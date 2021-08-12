import os
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

logLvl={
    "debug":logging.DEBUG,
    "info":logging.INFO,
    "warning":logging.INFO,
    "critical":logging.CRITICAL,
}

def getLogger(str="info"):
    log_dir = './logs'
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    # logger instance 생성
    logger = logging.getLogger(__name__)

    # formatter 생성
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')

    # handler 생성 (stream, file)
    streamHandler = logging.StreamHandler()
    fileHandler = TimedRotatingFileHandler(filename='./logs/test.log', when='midnight', interval=1, encoding='utf-8')
    fileHandler.setFormatter(formatter)
    fileHandler.suffix = '%Y%m%d'
    fileHandler.setLevel(logLvl[str])
    logger.addHandler(fileHandler)

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(logLvl[str])
    logger.addHandler(streamHandler)

    # logger instance에 fomatter 설정
    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # logger instance에 handler 설정
    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)
    logger.setLevel(level=logLvl[str])


    return logger
