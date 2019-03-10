#!/usr/bin/env python36
#-*- coding:utf-8 -*-

import logging
import logging.handlers



logger = logging.getLogger()
logfile = "logger.log"
hdlr = logging.handlers.RotatingFileHandler(logfile, 'a',  100000000,  5 , 'utf8', False)
formatter = logging.Formatter('%(asctime)s %(module)s %(funcName)s %(lineno)d %(levelname)s: %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(eval("logging."+'INFO'))

class logger_class:
	def __init__(self):
		pass
	def logging_info(self):
		print "log start"
		logging.debug('debug message')
		logging.info('info message')
		logging.warn('warn message')
		logging.error('error message')
		logging.critical('critical message') 

if __name__ == "__main__":
	print "begin"
	log = logger_class()
	log.logging_info()
