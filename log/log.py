# -*- coding: utf-8 -*-
# Time : 2024/2/25 10:20
# Author : lyz
# File : log.py
# Desc :
import logging
from config.config import log_file

#创建日志器
loggers = logging.getLogger()
#定义日志器的级别
loggers.setLevel(logging.INFO)
#定义处理器的格式
format=logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
#创建处理器
f= logging.FileHandler(log_file,mode='a',encoding='utf-8')
#设置处理器的级别
f.setLevel(logging.INFO)
f.setFormatter(format)
#把处理器加载到日志器
loggers.addHandler(f)
