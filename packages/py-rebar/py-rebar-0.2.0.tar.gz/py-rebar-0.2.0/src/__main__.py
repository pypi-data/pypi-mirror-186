"""Test appliction.

Running this script simulates a build + install + run of the module.
"""
from pyrebar.application import main
from pyrebar import Plugins
from importlib.metadata import EntryPoint
import sys

if __name__ == "__main__":
    """Bootstrap the plugins"""
    Plugins.add_entrypoint(
        EntryPoint(
            name="example-init",
            value="pyrebar.apps.example:initialize",
            group=Plugins.PREINIT_GROUP,
        )
    )
    Plugins.add_entrypoint(
        EntryPoint(
            name="example-init",
            value="pyrebar.apps.example:initialize",
            group=Plugins.POSTINIT_GROUP,
        )
    )
    Plugins.add_entrypoint(
        EntryPoint(
            name="example-init", value="pyrebar.apps.example", group=Plugins.APP_GROUP
        )
    )

    rc = main()
    sys.exit(rc)
