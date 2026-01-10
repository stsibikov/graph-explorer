import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


from logging_config import get_logger

logger = get_logger(__name__)


def run() -> str:
    from test_module import user_test

    user_test()
    return None


def main() -> None:
    try:
        run()
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Application failed: {e}", exc_info=True)
        sys.exit(1)
    return None


if __name__ == "__main__":
    main()
