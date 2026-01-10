from logging_config import get_logger

logger = get_logger()


def user_test():
    logger.info("user_test: logger worked")
    print("user_test: print worked")
    return None
