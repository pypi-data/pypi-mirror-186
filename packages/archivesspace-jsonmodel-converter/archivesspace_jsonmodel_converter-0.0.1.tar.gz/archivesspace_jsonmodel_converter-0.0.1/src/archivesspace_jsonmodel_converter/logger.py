import logging, os, re, sys
from copy import copy
import structlog
from pythonjsonlogger import jsonlogger

ROOT_LOGGER_NAME = 'aspace_jsonmodel_converter'

def copy_config(config):
    """Copy relevant information from one config to another."""

    new_config = {}
    new_logging = config["logging"].copy()
    new_structlog = {k: copy(v) for k, v in config["structlog"].items()}

    new_config.update(logging=new_logging, structlog=new_structlog)
    return new_config


# Regex to Match down or mixed-case usage of standard logging levels
canonical_levels = (
    "CRITICAL",
    "ERROR",
    "WARNING",
    "INFO",
    "DEBUG",
    "NOTSET",
)
level_re = re.compile(r"|".join((r"^{}$".format(level) for level in canonical_levels)), re.I)

stream_handler = None
file_handler=None
already_configured = False


def setup_logging(level=None, stream_json=True, filename=None):
    """sets up both logging and structlog."""
    global stream_handler, file_handler,  already_configured

    root_logger = logging.getLogger(ROOT_LOGGER_NAME)

    if stream_handler:
        root_logger.removeHandler(stream_handler)
    if file_handler:
        root_logger.removeHandler(file_handler)

    # Default configuration is info -> stdout - the ASPACE_JSONMODEL_CONVERTER_LOG_CONFIG var can be used to override default with pre-configured values
    from_env = os.environ.get("ASPACE_JSONMODEL_CONVERTER_LOG_CONFIG", None)

    level = level  or logging.INFO
    if isinstance(level, str) and level_re.match(level):
        level = getattr(logging, level.upper())

    config = {
        "logging": default_logging_conf(level=level),
        "structlog": default_structlog_conf(),
        "level": level,
    }

    # Forward what's needed to put the log places
    stream_handler = logging.StreamHandler(sys.stdout)
    if stream_json:
        stream_handler.setFormatter(jsonlogger.JsonFormatter())
    root_logger.addHandler(stream_handler)

    if filename:
        file_handler = logging.FileHandler(filename, mode="a")
        file_handler.setFormatter(jsonlogger.JsonFormatter())
        root_logger.addHandler(file_handler)
    root_logger.setLevel(level)
    structlog.reset_defaults()
    structlog.configure(**config["structlog"])
    already_configured = True


def get_logger(name=None):
    if not already_configured:
        setup_logging()

    # Make sure it's under the root logger
    if name and not name.startswith(ROOT_LOGGER_NAME + "."):
        name = f"{ROOT_LOGGER_NAME}.{name}"

    return structlog.get_logger(name or ROOT_LOGGER_NAME)


# Log format is standard across all provided defaults
# This amounts to a log of serialized JSON events with UTC timestamps and various
# useful information attached, which formats exceptions passed to logging methods in exc_info
def default_structlog_conf(**overrides):
    """Generate a default configuration for structlog"""
    conf = {
        "logger_factory": structlog.stdlib.LoggerFactory(),
        "wrapper_class": structlog.stdlib.BoundLogger,
        "cache_logger_on_first_use": True,
        "processors": [
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.stdlib.render_to_log_kwargs
        ],
    }
    conf.update(**overrides)
    return conf


def default_logging_conf(**overrides):
    """Generate a default stdlib logging configuration."""
    conf = {"level": logging.INFO}
    conf.update(**overrides)
    return conf
