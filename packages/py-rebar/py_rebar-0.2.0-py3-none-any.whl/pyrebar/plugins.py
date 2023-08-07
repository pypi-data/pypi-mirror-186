"""Load and manage application plugins."""
import dataclasses
import inspect
import itertools
import logging
import os.path
import sys
import toml
import typing

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points, EntryPoint, EntryPoints
else:
    from importlib.metadata import entry_points, EntryPoint, EntryPoints


@dataclasses.dataclass(frozen=True)
class PluginModule:
    """Plugin module data class, describing a plugin."""

    helpstr: str
    """The help string to display for this plugin."""
    command: str
    """The command to use on the command line."""
    conf: typing.Any
    """Function to configure the command line parameters."""
    func: typing.Any
    """The execution function for this plugin."""
    aliases: list
    """Various aliases for this module."""
    logger_name: str
    """Name of the logger to automatically configure."""


@dataclasses.dataclass(frozen=True)
class ProcessedPlugins:
    """Data after processing the various entrypoints."""

    pre_init: tuple[EntryPoint]
    """Pre-init plugin functions."""
    post_init: tuple[EntryPoint]
    """Post-init plugin functions."""
    apps: tuple[EntryPoint]
    """Application plugin modules."""
    shutdown: tuple[EntryPoint]
    """Post-application shutdown."""

    @staticmethod
    def loadapp(ep: EntryPoint) -> PluginModule:
        """Load an process an entrypoint into a plugin module.

        Args:
            ep (EntryPoint): The `EntryPoint` representing a plugin module.

        Returns:
            PluginModule: The processed plugin module.
        """
        module = ep.load()
        aliases = []
        helpstr = ""
        func = None
        conf = None
        command = ep.name
        logger_name = module.__name__

        for n, value in inspect.getmembers(module):
            if n == "__doc__":
                helpstr = value
            elif n == "SUBCOMMAND":
                command = value
            elif n == "config_args":
                conf = value
            elif n == "execute":
                func = value
            elif n == "ALIASES":
                aliases = value
            elif n == "LOGGER_NAME":
                logger_name = value

        return PluginModule(
            helpstr=helpstr,
            func=func,
            conf=conf,
            command=command,
            aliases=aliases,
            logger_name=logger_name,
        )


_PREINIT_GROUP = "{prefix}.preinit"
_POSTINIT_GROUP = "{prefix}.postinit"
_APP_GROUP = "{prefix}.app"
_SHUTDOWN_GROUP = "{prefix}.shutdown"


@dataclasses.dataclass(frozen=True)
class PluginGroups:
    """Various entrypoint groups based on the provided prefix."""

    pre_init: str
    """Group used for the pre-init step."""
    post_init: str
    """Group used for the post-init step."""
    app: str
    """Group used for applications."""
    shutdown: str
    """Group used for the post-application shutdown."""

    @classmethod
    def with_prefix(cls, prefix: str = "pyrebar"):
        """Create a class with the provided prefix.

        Args:
            prefix (str, optional): The prefix. Defaults to "pyrebar".

        Returns:
            PluginGroups: The new PluginGroups instance.
        """
        if not prefix:
            prefix = "pyrebar"
        return cls(
            pre_init=_PREINIT_GROUP.format(prefix=prefix),
            post_init=_POSTINIT_GROUP.format(prefix=prefix),
            app=_APP_GROUP.format(prefix=prefix),
            shutdown=_SHUTDOWN_GROUP.format(prefix=prefix),
        )


class Plugins:
    """Module enabling bootstrapping the `entry_points()` list."""

    __entrypoints: list[EntryPoint] = []

    @staticmethod
    def groups(prefix: str = None) -> PluginGroups:
        """Create a groups object with the optional prefix.

        Args:
            prefix (str, optional): Optional prefix to append. If `None`, the default
            prefix 'pyrebar' will be used. Defaults to None.

        Returns:
            PluginGroups: The groups instance.
        """
        return PluginGroups.with_prefix(prefix=prefix)

    @classmethod
    def add_entrypoint(cls, ep: EntryPoint):
        """Explicitly add an entrypoint.

        These `EntryPoint` instances will be provided in addition to the results of those
        from the importlib metadata module.  Call this method to bootstrap applications
        running from `__main__` rather than as an installed module.

        Args:
            ep (EntryPoint): The entrypoint to add.
        """
        if ep:
            cls.__entrypoints.append(ep)

    @classmethod
    def entry_points(cls) -> EntryPoints:
        """Provide entry points from the installed modules.

        This method aggregates the installed modules with any included via
        bootstrapping.

        Returns:
            EntryPoints: The resulting entrypoints
        """
        points = entry_points()

        if cls.__entrypoints:
            pts = list(itertools.chain(*[points.select(name=n) for n in points.names]))
            pts.extend(cls.__entrypoints)
            points = EntryPoints(pts)

        return points

    @classmethod
    def extract_plugins(
        cls, prefix: str = "pyrebar", groups: PluginGroups = None
    ) -> ProcessedPlugins:
        """Extract the py-rebar plugins from the entrypoints.

        Returns:
            ProcessedPlugins: The processed entrypoints
        """
        entry_points = cls.entry_points()
        if not groups:
            groups = PluginGroups.with_prefix(prefix=prefix)

        pre_init = tuple(e for e in entry_points.select(group=groups.pre_init))
        post_init = tuple(e for e in entry_points.select(group=groups.post_init))
        apps = tuple(e for e in entry_points.select(group=groups.app))
        shutdown = tuple(e for e in entry_points.select(group=groups.shutdown))

        return ProcessedPlugins(
            pre_init=pre_init, post_init=post_init, apps=apps, shutdown=shutdown
        )


def bootstrap_from_pyproject(path: str = "pyproject.toml"):
    """Bootstrap the plugins using the entrypoints found in pyproject.toml.

    Args:
        path (str, optional): Path to the pyproject.toml file. Defaults
        to pyproject.toml.
    """
    if not os.path.exists(path):
        logging.getLogger(__name__).warning(
            "Aborting py-prebar bootstrap, pyproject.toml not found. path=%s", path
        )
        return

    pyproj = toml.load(path)

    if "project" not in pyproj:
        return

    proj = pyproj["project"]

    if "entry-points" not in proj:
        return

    for group, points in proj["entry-points"].items():
        for name, value in points.items():
            ep = EntryPoint(name=name, value=value, group=group)
            Plugins.add_entrypoint(ep)
