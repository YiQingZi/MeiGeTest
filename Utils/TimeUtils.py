# -*- coding: utf-8 -*-

import time


class TimeUtils:


    @staticmethod
    def Time_calc(startTime):
        """
        计算时差，单位毫秒
        """
        endTime = time.time()
        endTime = int(round(endTime * 1000))
        Time = endTime - startTime
        return Time

    @staticmethod
    def Time_ms():
        """
        获得毫秒时间戳
        """
        startTime = time.time()
        startTime = int(round(startTime * 1000))
        return startTime


    @staticmethod
    def strTimeName():
        """
        格式化时间，返回当前时间
        """
        t = time.localtime(time.time())
        strT = time.strftime('%Y-%m-%d-%H-%M-%S', t)
        #%Y-%m-%d-%H-%M-%S  Y 年  m月 d日  H时 M分 S秒
        return str(strT)
        
    @staticmethod
    def strTime():
        """
        格式化时间，返回当前时间
        """
        t = time.localtime(time.time())
        strT = time.strftime('%Y-%m-%d  %H:%M:%S', t)
        #%Y-%m-%d-%H-%M-%S  Y 年  m月 d日  H时 M分 S秒
        return str(strT)