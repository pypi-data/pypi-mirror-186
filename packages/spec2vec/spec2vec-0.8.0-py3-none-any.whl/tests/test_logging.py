# -*- coding: utf-8 -*-
import logging
import os
from spec2vec.logging_functions import (add_logging_to_file,
                                        reset_spec2vec_logger,
                                        set_spec2vec_logger_level)


def test_initial_logging(caplog, capsys):
    """Test logging functionality."""
    reset_spec2vec_logger()
    logger = logging.getLogger("spec2vec")
    logger.info("info test")
    logger.warning("warning test")
    assert logger.name == "spec2vec", "Expected different logger name"
    assert logger.getEffectiveLevel() == 30, "Expected different logging level"
    assert "info test" not in caplog.text, "Info log should not be shown."
    assert "warning test" in caplog.text, "Warning log should have been shown."
    assert "warning test" in capsys.readouterr().out, \
        "Warning log should have been shown to stderr/stdout."
    reset_spec2vec_logger()


def test_set_and_reset_spec2vec_logger_level(caplog):
    """Test logging functionality."""
    logger = logging.getLogger("spec2vec")
    assert logger.getEffectiveLevel() == 30, "Expected different logging level"

    set_spec2vec_logger_level("INFO")
    logger.debug("debug test")
    logger.info("info test")

    assert logger.name == "spec2vec", "Expected different logger name"
    assert logger.getEffectiveLevel() == 20, "Expected different logging level"
    assert "debug test" not in caplog.text, "Debug log should not be shown."
    assert "info test" in caplog.text, "Info log should have been shown."

    reset_spec2vec_logger()
    assert logger.getEffectiveLevel() == 30, "Expected different logging level"
    reset_spec2vec_logger()


def test_add_logging_to_file(tmp_path, caplog, capsys):
    """Test writing logs to file."""
    reset_spec2vec_logger()
    set_spec2vec_logger_level("INFO")
    filename = os.path.join(tmp_path, "test.log")
    add_logging_to_file(filename)
    logger = logging.getLogger("spec2vec")
    logger.info("test message no.1")

    expected_log_entry = "test message no.1"
    # Test streamed logs
    assert expected_log_entry in caplog.text, "Expected different log message."
    assert expected_log_entry in capsys.readouterr().out, \
        "Expected different log message in output (stdout/stderr)."

    # Test log file
    expected_log_entry = "INFO:spec2vec:test_logging:test message no.1"
    assert len(logger.handlers) == 2, "Expected two Handler"
    assert os.path.isfile(filename), "Log file not found."
    with open(filename, "r", encoding="utf-8") as file:
        logs = file.read()
    assert expected_log_entry in logs, "Expected different log file content"
    reset_spec2vec_logger()


def test_add_logging_to_file_only_file(tmp_path, capsys):
    """Test writing logs to file."""
    reset_spec2vec_logger()
    set_spec2vec_logger_level("INFO")
    filename = os.path.join(tmp_path, "test.log")
    add_logging_to_file(filename, remove_stream_handlers=True)
    logger = logging.getLogger("spec2vec")
    logger.info("test message no.1")

    # Test streamed logs
    not_expected_log_entry = "test message no.1"
    assert len(logger.handlers) == 1, "Expected only one Handler"
    assert not_expected_log_entry not in capsys.readouterr().out, "Did not expect log message"

    # Test log file
    expected_log_entry = "INFO:spec2vec:test_logging:test message no.1"
    assert os.path.isfile(filename), "Log file not found."
    with open(filename, "r", encoding="utf-8") as file:
        logs = file.read()
    assert expected_log_entry in logs, "Expected different log file content"
    reset_spec2vec_logger()
