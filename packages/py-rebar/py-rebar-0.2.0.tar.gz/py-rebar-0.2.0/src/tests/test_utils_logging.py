"""Unit tests for utils/logging.py."""
import argparse
import copy
from unittest.mock import patch
import pytest

import pyrebar.utils.logging


@pytest.fixture(autouse=True)
def test_config():
    """Fixture for the logging configuration."""
    config = copy.deepcopy(pyrebar.utils.logging.CONFIG)
    yield pyrebar.utils.logging.CONFIG
    pyrebar.utils.logging.CONFIG = config


def test_config_args():
    """Verify creating the command-line arguments."""
    parser = argparse.ArgumentParser()
    pyrebar.utils.logging.config_args(parser)

    # verify the log levels
    for param, expected in (
        (None, "INFO"),
        ("--quiet", "CRITICAL"),
        ("--critical", "CRITICAL"),
        ("--error", "ERROR"),
        ("--warn", "WARNING"),
        ("--warning", "WARNING"),
        ("--info", "INFO"),
        ("--debug", "DEBUG"),
    ):
        args = parser.parse_args([param] if param else [])
        assert expected == args.log_level
        assert not args.log_root_level

    # verify the root log levels
    for param, expected in (
        ("--root-quiet", "CRITICAL"),
        ("--root-critical", "CRITICAL"),
        ("--root-error", "ERROR"),
        ("--root-warn", "WARNING"),
        ("--root-warning", "WARNING"),
        ("--root-info", "INFO"),
        ("--root-debug", "DEBUG"),
    ):
        args = parser.parse_args([param] if param else [])
        assert "INFO" == args.log_level
        assert expected == args.log_root_level


@patch("pyrebar.utils.logging.logging.config.dictConfig")
def test_config_logging_noargs(mock_logging_config, test_config):
    """Verify logging is configured without args."""
    expected = copy.deepcopy(test_config)
    expected["loggers"][""]["level"] = "ERROR"

    pyrebar.utils.logging.config_logging(None)

    mock_logging_config.assert_called_with(expected)


@patch("pyrebar.utils.logging.logging.config.dictConfig")
def test_config_logging_rootinfo(mock_logging_config, test_config):
    """Verify logging is configured with the root log level set to info."""
    expected = copy.deepcopy(test_config)
    expected["loggers"][""]["level"] = "INFO"

    pyrebar.utils.logging.config_logging(argparse.Namespace(log_root_level="INFO"))

    mock_logging_config.assert_called_with(expected)


@patch("pyrebar.utils.logging.logging.config.dictConfig")
def test_config_logging_info(mock_logging_config, test_config):
    """Verify logging is configured with the log level set to info."""
    expected = copy.deepcopy(test_config)
    expected["loggers"][""]["level"] = "INFO"

    pyrebar.utils.logging.config_logging(
        argparse.Namespace(log_level="INFO", log_root_level="ERROR")
    )

    mock_logging_config.assert_called_with(expected)


@patch("pyrebar.utils.logging.logging.config.dictConfig")
def test_config_logging_name(mock_logging_config, test_config):
    """Verify logging is configured with the logger name set."""
    expected = copy.deepcopy(test_config)
    expected["loggers"][""]["level"] = "ERROR"
    expected["loggers"]["yellowbeard"] = copy.deepcopy(expected["loggers"][""])
    expected["loggers"]["yellowbeard"]["level"] = "INFO"

    pyrebar.utils.logging.config_logging(
        argparse.Namespace(
            log_level="INFO", log_root_level="ERROR", logger_name="yellowbeard"
        )
    )

    mock_logging_config.assert_called_with(expected)


@patch("pyrebar.utils.logging.logging.config.dictConfig")
def test_config_logging_func(mock_logging_config, test_config):
    """Verify logging is configured with a logger name inferred from function."""
    expected = copy.deepcopy(test_config)
    expected["loggers"][""]["level"] = "ERROR"
    expected["loggers"]["tests.test_utils_logging"] = copy.deepcopy(
        expected["loggers"][""]
    )
    expected["loggers"]["tests.test_utils_logging"]["level"] = "INFO"

    pyrebar.utils.logging.config_logging(
        argparse.Namespace(
            log_level="INFO", log_root_level="ERROR", func=test_config_logging_func
        )
    )

    mock_logging_config.assert_called_with(expected)
