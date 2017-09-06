#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/2017 10:55 AM
# @Author  : Winnichen
# @File    : log_writer.py
import time
from config import settings
def initlog():
    import logging
    import logging.handlers
    logger = logging.getLogger()
    fmt='%Y-%m-%d'
    Date=time.strftime(fmt,time.localtime(time.time()))
    LOG_FILE = settings.logfile_prefix+Date
    hdlr=logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    return logger

logging = initlog()