# coding=utf-8
import os
import re
import sys
import uuid
import time
import random
import string
import inspect
import hashlib
import platform



# Print tools
def _print(message, code=None, tag=None, end=None):
    if tag is None:
        message = '[{}] {}'.format(tag, message)
    if code is not None:
        message = '\033[0;{}m{}\033[0m'.format(code, message)
    print(message, end=end)


def print_red(message, tag="ERROR", end=None):
    _print(message, 31, tag, end)  # 红色


def print_green(message, tag="DONE", end='\n'):
    _print(message, 32, tag, end)  # 绿色


def print_yellow(message, tag="WARNING", end='\n'):
    _print(message, 33, tag, end)  # 黄色


def print_blue(message, tag="BEG", end='\n'):
    _print(message, 34, tag, end)  # 深蓝色


def print_purple(message, tag="MID", end='\n'):
    _print(message, 35, tag, end)  # 紫色


def print_azure(message, tag="END", end='\n'):
    _print(message, 36, tag, end)  # 浅蓝色


def print_white(message, tag="INFO", end='\n'):
    _print(message, 37, tag, end)  # 白色


def print_none(message, tag="DEBUG", end='\n'):
    _print(message, None, tag, end)  # 默认


def process_bar(now, total, attach=''):
    # 在窗口底部动态显示进度条
    rate = now / total
    rate_num = int(rate * 100)
    bar_length = int(rate_num / 2)
    if rate_num == 100:
        bar = 'Pid:[%5d]: %s' % (os.getpid(), attach.center(10, " "))
        bar = '\r' + bar[0:40]
        bar += '%s>%d%%\n' % ('=' * bar_length, rate_num)
    else:
        bar = 'Pid:[%5d]: %s' % (os.getpid(), attach.center(10, " "))
        bar = '\r' + bar[0:40]
        bar += '%s>%d%%' % ('=' * bar_length, rate_num)
    sys.stdout.write(bar)
    sys.stdout.flush()

