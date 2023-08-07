"""Configure the python logger."""
import logging
import logging.config


CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        }
    },
    "handlers": {
        "standard": {"class": "logging.StreamHandler", "formatter": "standard"}
    },
    "loggers": {
        "": {
            "handlers": ["standard"],
            "level": "ERROR",
            "propagate": False,
        }
    },
}
"""Config dictionary."""


def config_args(parser):
    """Add command line arguments for logging.

    Args:
        parser (argparse.ArgumentParser): The command line parser.
    """
    loglevel = parser.add_argument_group(
        title="Log level", description="Set detail level of application log output."
    ).add_mutually_exclusive_group()
    loglevel.add_argument(
        "--quiet",
        "--critical",
        action="store_const",
        const="CRITICAL",
        dest="log_level",
        help="Suppress all but the most critical log statements.",
    )

    loglevel.add_argument(
        "--error",
        action="store_const",
        const="ERROR",
        dest="log_level",
        help="Display error logs.",
    )
    loglevel.add_argument(
        "--warn",
        "--warning",
        action="store_const",
        const="WARNING",
        dest="log_level",
        help="Display error and warning logs.",
    )
    loglevel.add_argument(
        "--info",
        action="store_const",
        const="INFO",
        dest="log_level",
        help="Print informational logging.",
    )
    loglevel.add_argument(
        "--debug",
        action="store_const",
        const="DEBUG",
        dest="log_level",
        help="Display highly detailed level of logging.",
    )

    loglevel = parser.add_argument_group(
        title="Root log level", description="Set detail level of root log output."
    ).add_mutually_exclusive_group()
    loglevel.add_argument(
        "--root-quiet",
        "--root-critical",
        action="store_const",
        const="CRITICAL",
        dest="log_root_level",
        help="Suppress all but the most critical log statement.",
    )

    loglevel.add_argument(
        "--root-error",
        action="store_const",
        const="ERROR",
        dest="log_root_level",
        help="Display error logs.",
    )
    loglevel.add_argument(
        "--root-warn",
        "--root-warning",
        action="store_const",
        const="WARNING",
        dest="log_root_level",
        help="Display error and warning logs.",
    )
    loglevel.add_argument(
        "--root-info",
        action="store_const",
        const="INFO",
        dest="log_root_level",
        help="Print informational logging.",
    )
    loglevel.add_argument(
        "--root-debug",
        action="store_const",
        const="DEBUG",
        dest="log_root_level",
        help="Display highly detailed level of logging.",
    )
    parser.set_defaults(log_root_level=None, log_level="INFO")


def config_logging(args=None):
    """Configure logging based on the provided command line arguments.

    Args:
        args (argparse.Namespace, optional): The parsed command line arguments.
        Defaults to None.
    """
    app_logger_name = None
    if args:
        if "logger_name" in args and args.logger_name is not None:
            app_logger_name = args.logger_name
        elif "func" in args and args.func:
            m: str = args.func.__module__
            f: str = args.func.__name__
            app_logger_name = m.removesuffix(f".{f}")

    root_level = _arg_or_default(args, "log_root_level", "ERROR")

    if app_logger_name:
        CONFIG["loggers"][app_logger_name] = {
            "handlers": ["standard"],
            "level": _arg_or_default(args, "log_level", "INFO"),
            "propagate": False,
        }
    else:
        root_level = _arg_or_default(args, "log_level", root_level)

    CONFIG["loggers"][""]["level"] = root_level

    logging.config.dictConfig(CONFIG)


def _arg_or_default(args, key: str, default=None):
    if args and key in args:
        v = vars(args)[key]
        return v or default
    else:
        return default
