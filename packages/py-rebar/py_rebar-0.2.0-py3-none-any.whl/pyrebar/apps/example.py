"""Example application."""
import logging

SUBCOMMAND = "example-command"
"""Override the default subcommand name. Remove if unnecessary."""

ALIASES = ["exc"]
"""Add subcommand aliases."""

LOGGER_NAME = "pyrebar.apps"


def initialize(**kwargs):
    """Initialize the framework."""
    print("Initialized the pirate ship")


def config_args(parser):
    """Add example command line parameters."""
    parser.add_argument("--pillage", help="Pillage in piratey ways.")


def execute(args=None) -> int:
    """An example application.

    This function performs a basic thing that does stuff.
    """
    logger = logging.getLogger(__name__)

    print(__name__)

    print("Yay example!")

    logger.info("completed.")
    return 0


def shutdown():
    """Shutdown hook."""
    print("shutdown hook")
