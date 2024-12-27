import logging

def get_logger(log_file: str = 'logs/automation.logs', log_level: int = logging.DEBUG):
    """
    Configure the logger with file and console handlers.

    :param log_file: The log file where the logs will be saved.
    :param log_level: The logging level. Default is DEBUG.
    :return: Configured logger.
    """
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Create file handler for logging to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # Create console handler for logging to the console (optional)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Log level for console (INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
