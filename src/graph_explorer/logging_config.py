import logging
import sys


def get_logger(name: str | None = None, level: str | None = None) -> logging.Logger:
    """
    Production-ready logger factory for the multi-module pattern.

    - First call configures root logger (stdout, handlers, format)
    - Subsequent calls return named loggers that inherit root config
    - Use in src/__init__.py first, then in all modules

    Args:
        name: Logger name (defaults to __name__ if called from module)
        level: Optional level override for this logger only

    Returns:
        Pre-configured logger instance
    """
    # Use __name__ if no explicit name provided (module-level usage)
    if name is None:
        name = __name__

    logger = logging.getLogger(name)

    # Configure root only once (idempotent)
    if not logging.getLogger().handlers:
        formatter = logging.Formatter("%(asctime)s.%(msecs)03d %(levelname)-8s [%(name)s:%(lineno)d] %(message)s")

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)

        root = logging.getLogger()
        root.handlers.clear()
        root.addHandler(handler)
        root.setLevel(logging.DEBUG)

    # Apply level override if specified
    if level:
        logger.setLevel(level)

    logger.propagate = True  # Inherit root handlers

    return logger
