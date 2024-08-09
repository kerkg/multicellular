import logging.handlers
import sys


def default_logger_configuration_for_logging(name: str):  # made entirely by pieces copilot and run on the first try (yes its awesome)
    # make Logger
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)  # accept logs from all levels

    # make Formatter
    __formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # STDERR Handler (for ERROR ve CRITICAL logs)
    __stderr_handler = logging.StreamHandler(sys.stderr)
    __stderr_handler.setLevel(logging.ERROR)
    __stderr_handler.setFormatter(__formatter)
    logger.addHandler(__stderr_handler)

    # Rotating File Handler (for other logs)
    __file_handler = logging.handlers.RotatingFileHandler(
        'app.log', maxBytes=3*1024*1024, backupCount=3)
    __file_handler.setLevel(logging.DEBUG)
    __file_handler.setFormatter(__formatter)
    logger.addHandler(__file_handler)

    return logger


# Test logger
if __name__ == '__main__':
    logger = default_logger_configuration_for_logging()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')