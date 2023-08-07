"""Application framework."""
import argparse
import logging
import pyrebar.utils.logging

from .plugins import Plugins, ProcessedPlugins, PluginModule


def _add_app(parser: argparse.ArgumentParser, plugin: PluginModule):
    if plugin.func:
        parser.set_defaults(func=plugin.func, logger_name=plugin.logger_name)
    else:
        parser.set_defaults(func=lambda **kwargs: None, logger_name="")

    if plugin.conf:
        plugin.conf(parser)


def main(argv=None, plugin_prefix: str = None) -> int:
    """The main application.

    Returns:
        int: The return value.
    """
    plugins = Plugins.extract_plugins(prefix=plugin_prefix)
    parser = argparse.ArgumentParser()

    # add the pyrebar logging parameters
    pyrebar.utils.logging.config_args(parser)

    try:
        # pre-init
        for e in plugins.pre_init:
            e.load()(parser=parser)

        # load plugins
        if not plugins.apps:
            raise ModuleNotFoundError(
                "No apps loaded. Verify a business logic application is installed."
            )
        elif len(plugins.apps) == 1:
            plugin = ProcessedPlugins.loadapp(plugins.apps[0])
            _add_app(parser, plugin)
        else:
            subparsers = parser.add_subparsers(
                title="Subcommands",
                description="Valid subcommands.",
                help="Specify {subcommand} --help for more details",
            )

            for e in plugins.apps:
                plugin = ProcessedPlugins.loadapp(e)
                if plugin.func:
                    p = subparsers.add_parser(
                        plugin.command, help=plugin.helpstr, aliases=plugin.aliases
                    )
                    _add_app(p, plugin)

        # process arguments
        args = parser.parse_args(args=argv)

        # configure the logger
        pyrebar.utils.logging.config_logging(args)

        # post-init
        for e in plugins.post_init:
            e.load()(args=args)

        # execute the selected plugin
        if args.func:
            return args.func(args=args)
        else:
            raise RuntimeError("No subcommand specified, use --help for more info.")

    finally:
        for e in plugins.shutdown:
            try:
                e.load()()
            except:  # noqa: E722 - log shutdown errors
                logging.getLogger(__name__).error(
                    "Caught error executing shutdown hook %s",
                    e.name,
                    exc_info=1,
                    stack_info=1,
                )
