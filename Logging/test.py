import logging
import slash.log
import logbook

# Enable colorization of log files
slash.config.root.log.colorize = True

# Set the color for logs from 'my_logger_name' with log level INFO to 'red'
slash.log.set_log_color('my_logger_name', logbook.NOTICE, 'red')

# Create a custom logger named 'my_logger_name'
my_logger = logging.getLogger('my_logger_name')

# Add a log handler to the custom logger
my_logger.addHandler(logging.StreamHandler())

# Example usage of the custom logger
my_logger.debug('This is a debug message')
my_logger.info('This is an info message')  # This should appear red
my_logger.warning('This is a warning message')
my_logger.error('This is an error message')
my_logger.critical('This is a critical message')

def test_addition():
    assert 2+2 == 4
