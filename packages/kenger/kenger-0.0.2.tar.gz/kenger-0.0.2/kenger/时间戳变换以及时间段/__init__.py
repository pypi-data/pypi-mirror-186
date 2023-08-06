# coding=utf-8
import datetime
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



# Time tools

# 获取当前时间戳
def unix_time(unit=1):
    return int(time.time() * unit)


def str_time(pattern='%Y-%m-%d %H:%M:%S', timing=None):
    if timing is None:
        timing = time.time()
    return time.strftime(pattern, time.localtime(timing))


def format_time(time_obj, pattern='%Y-%m-%d %H:%M:%S'):
    return time.strftime(pattern, time_obj)


# datetime 转化为unix（也就是时间戳）
def datetime_to_unix(timing):
    return int(time.mktime(timing.timetuple()))


# 字符串时间与timestamp之间的转换
def timestr_to_timestamp(time_string, pattern='%Y-%m-%d %H:%M:%S'):
    time_array = time.strptime(time_string, pattern)
    return int(time.mktime(time_array))


def timestamp_to_timestr(u_time, pattern='%Y-%m-%d %H:%M:%S'):
    return time.strftime(pattern, time.localtime(u_time))



# 输出一段时间之间的每一天，无0
def deal_no_zero(begin_date, end_date, pattern = "%Y.%m.%d"):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, pattern)
    end_date = datetime.datetime.strptime(end_date, pattern)
    while begin_date <= end_date:
        date_str = str(begin_date.year) + '.' + str(begin_date.month) + '.' + str(begin_date.day)
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    print(date_list)
    return date_list


# 输出一段时间之间的每一天
def deal_with_zero(begin_date, end_date, pattern = "%Y-%m-%d"):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, pattern)
    end_date = datetime.datetime.strptime(end_date, pattern)
    while begin_date <= end_date:
        date_str = begin_date.strftime(pattern)
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    print(date_list)
    return date_list



if __name__ == '__main__':
    ans = timestr_to_timestamp('2020-12-19 10:30:09')
    print(ans)
    print(unix_time())

    # now = datetime.datetime.now()
    # print(datetime_to_unix(now))

    deal('2021.2.2', '2022.12.21')


    

