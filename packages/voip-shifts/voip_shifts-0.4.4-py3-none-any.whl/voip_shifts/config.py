from redis import Redis
from redis.exceptions import AuthenticationError
from rq import Queue
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
import telnyx

import os
import logging

class Config:

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", 
        "postgresql://postgres:root@127.0.0.1/vp22_backend")
    REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "redis")
    REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
    REDIS_DB = os.environ.get("REDIS_DB", 0)
    BOT_KEY = os.environ.get("BOT_KEY")
    assert BOT_KEY, "BOT_KEY is not specified"
    #! If don't need => then remove
    SIP_PASSWORD = os.environ.get("SIP_PASSWORD")
    assert SIP_PASSWORD, "SIP_PASSWORD is not specified"
    SIP_USERNAME = os.environ.get("SIP_USERNAME")
    assert SIP_USERNAME, "SIP_USERNAME is not specified"
    SIP_SERVER = os.environ.get("SIP_SERVER")
    assert SIP_SERVER, "SIP_SERVER is not specified"
    MODE = os.environ.get("DEPLOY_MODE", "dev")


log = logging.getLogger()
log.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
fileHandler = logging.FileHandler("./INFO.log")
formatter = logging.Formatter('%(levelname)s:%(asctime)s :: %(message)s', "%Y-%m-%d %H:%M:%S")
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
log.addHandler(streamHandler)
log.addHandler(fileHandler)


redis = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, 
              db=Config.REDIS_DB, password=Config.REDIS_PASSWORD)

rq = Queue("high", connection=redis)
Base = declarative_base()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)
