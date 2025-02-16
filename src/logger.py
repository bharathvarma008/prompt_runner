import logging
import os
import json
from datetime import datetime
from logging.handlers import RotatingFileHandler

class JSONFormatter(logging.Formatter):
    def format(self, record):
        # Create log record with specific fields
        log_obj = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage()
        }
        
        # Add extra fields if they exist
        if hasattr(record, 'prompt'):
            log_obj['input_prompt'] = record.prompt
        if hasattr(record, 'response'):
            log_obj['api_response'] = record.response

        return json.dumps(log_obj, ensure_ascii=False)  # Removed the trailing comma

class JSONRotatingFileHandler(RotatingFileHandler):
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None):
        super().__init__(filename, mode, maxBytes, backupCount, encoding)
        # Write the opening bracket for the JSON array
        if os.path.getsize(filename) == 0:
            self.stream.write('[\n')
        self.first_record = True

    def emit(self, record):
        """Override emit to handle JSON array formatting"""
        if not self.first_record:
            self.stream.write(',\n')  # Add comma and newline before new records
        else:
            self.first_record = False
        
        super().emit(record)

    def doRollover(self):
        if self.stream is not None:
            self.stream.write('\n]\n')  # Close the JSON array
            self.stream.flush()
        super().doRollover()
        self.stream.write('[\n')  # Start new file with opening bracket
        self.first_record = True

    def close(self):
        if self.stream is not None:
            self.stream.write('\n]\n')  # Close the JSON array properly
            self.stream.flush()
        super().close()

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        # Move prompt and response from kwargs to extra
        extra = kwargs.get('extra', {})
        if 'prompt' in kwargs:
            extra['prompt'] = kwargs.pop('prompt')
        if 'response' in kwargs:
            extra['response'] = kwargs.pop('response')
        kwargs['extra'] = extra
        return msg, kwargs

class Logger:
    def __init__(self):
        # Create logs directory if it doesn't exist
        self.logs_dir = "logs"
        if not os.path.exists(self.logs_dir):
            os.makedirs(self.logs_dir)

        # Create timestamp for file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create logger
        self._logger = logging.getLogger('OpenAILogger')
        self._logger.setLevel(logging.DEBUG)

        # Create formatters
        json_formatter = JSONFormatter()
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')

        # JSON File handler
        json_log_file = os.path.join(self.logs_dir, f'openai_app_{timestamp}.json')
        json_file_handler = JSONRotatingFileHandler(
            json_log_file,
            maxBytes=1024 * 1024,
            backupCount=5
        )
        json_file_handler.setLevel(logging.DEBUG)
        json_file_handler.setFormatter(json_formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)

        # Add handlers
        self._logger.addHandler(json_file_handler)
        self._logger.addHandler(console_handler)

        # Create adapter
        self.logger = CustomAdapter(self._logger, {})

    def _log_with_context(self, level, message, **kwargs):
        """Helper method to log with additional context"""
        extra = {
            'prompt': kwargs.get('prompt'),
            'response': kwargs.get('response')
        }
        self.logger.log(level, message, extra=extra)

    def debug(self, message, **kwargs):
        self._log_with_context(logging.DEBUG, message, **kwargs)

    def info(self, message, **kwargs):
        self._log_with_context(logging.INFO, message, **kwargs)

    def warning(self, message, **kwargs):
        self._log_with_context(logging.WARNING, message, **kwargs)

    def error(self, message, **kwargs):
        self._log_with_context(logging.ERROR, message, **kwargs)

    def critical(self, message, **kwargs):
        self._log_with_context(logging.CRITICAL, message, **kwargs)

# Create a singleton instance
logger = Logger().logger 