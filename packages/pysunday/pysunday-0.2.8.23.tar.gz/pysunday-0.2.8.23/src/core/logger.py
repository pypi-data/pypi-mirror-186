# coding: utf-8
import logging
import colorlog
import atexit
import datetime
from os import path
from sunday.core.globalvar import getvar, setvar
from sunday.core.getConfig import getConfig
import sunday.core.paths as paths
from sunday.core.globalKeyMaps import sdvar_loggerid, sdvar_logger, sdvar_loglevel

if not getvar(sdvar_loggerid):
    loggerId = datetime.datetime.today().isoformat()
    setvar(sdvar_loggerid, loggerId)
    if getConfig('LOGGING')('print_file'):
        @atexit.register
        def exitPrintLogfile():
            getvar(sdvar_logger).info('LOG FILE AT: %s' % path.join(paths.logCwd, loggerId))

logLevelKeys = ['notset', 'debug', 'info', 'warning', 'error', 'critical']

logfile = path.join(paths.logCwd, getvar(sdvar_loggerid))

logging.basicConfig(filename=logfile, level=logging.DEBUG, force=True,
        format='[%(asctime)s.%(msecs)-3d] %(levelname)s <%(name)s>: %(message)s')

class Logger():
    def __init__(self, name, level='', format=''):
        cfg = getConfig('LOGGING')
        logger = logging.getLogger(name)
        if not logger.handlers:
            loglevel = level or getvar(sdvar_loglevel) or cfg('level') or 'error'
            logger.setLevel(logging.getLevelName(loglevel.upper()))
            loghd = logging.StreamHandler()
            loghd.setFormatter(colorlog.ColoredFormatter(format or cfg('format'), datefmt='%H:%M:%S'))
            logger.addHandler(loghd)
            logger.propagate = True
        self.logger = logger

    def getLogger(self):
        return self.logger

def setLogLevel(level):
    # 设置所有日志管理者的日志等级
    setvar(sdvar_loglevel, level)
    levelstr = level.upper()
    level = getattr(logging, levelstr)
    handlerList = logging.Logger.manager.loggerDict.values()
    for handler in handlerList:
        if hasattr(handler, 'setLevel') and handler.level != level:
            handler.setLevel(level)
