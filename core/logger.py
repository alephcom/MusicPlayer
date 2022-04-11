import logging
import json
import logging.handlers as handlers
from pythonjsonlogger import jsonlogger
from pyrogram.types import Message
from core.song import Song

def create_logger(file_path : str, logger_name : str):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    loggerHandler = handlers.RotatingFileHandler(file_path, maxBytes=10*1024*1024,
                                    backupCount=1)
    loggerHandler.setLevel(logging.INFO)
    loggerHandler.setFormatter(jsonlogger.JsonFormatter())

    logger.addHandler(loggerHandler)

    return logger

def log_bot_requests(message : Message):
    json_message = json.loads(str(message))
    requestsLogger.info(message.text, extra={"detail_message" : json_message})

def log_stream_actions(song : Song, action : str):
    streamLogger.info(action, extra = song.to_dict())

# create a bot requests logging
requestsLogger = create_logger('logs/requests.log', 'requests')
# create a stream action logging
streamLogger = create_logger('logs/stream.log', 'stream')
