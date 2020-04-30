# -*- coding: utf-8 -*-

import hashlib
import sys
import time

from Basics.Command import run_command
from Basics.Version import Python_version
import logging
import os


class Utils:

    @staticmethod
    def get_FileSize(filePath):
        """
        返回文件大小 MB
        """
        try:
            filesize = os.path.getsize(filePath)
            filesize = filesize / float(1024 * 1024)
            return round(filesize, 2)
        except IOError as err:
            logging.warning(err)
            return 0

    @staticmethod
    def get_sys_path():
        """
        返回运行路径
        """
        return str(sys.path[0])

    @staticmethod
    def get_android_Tcard_path(dev, logon=True):
        """
        返回设备T卡路径
        """
        result, out = run_command("adb -s {0} shell ls storage".format(dev), logon)
        out = out.split('\n')
        for x in out:
            if '-' in x:
                out = x
                break
            out = None
        # out = re.sub(r'\n','',out)
        return result, out

    @staticmethod
    def adbshell(dev, command_line, logon=False):
        """
        adb shell 命令
        """
        result, out = run_command("adb -s {0} shell {1}".format(dev, command_line), logon)
        return result, out

    @staticmethod
    def adb(dev, command_line, logon=False):
        """
        adb shell 命令
        """
        result, out = run_command("adb -s {0} {1}".format(dev, command_line), logon)
        return result, out

    @staticmethod
    def saveTxtFile(fileName='Null', mode='a+', data='Null'):
        """
        保存文本文档
        """
        v = Python_version()
        logging.debug(fileName)
        if v > 3.0:
            with open(fileName, mode, encoding='UTF-8') as f:
                f.write(data)
        else:
            f = open(fileName, mode)
            f.write(data)

    @staticmethod
    def md5_calc(file):
        """
        检验文件MD5码
        """
        md5_value = hashlib.md5()
        with open(file, 'rb') as file_b:
            while True:
                data_flow = file_b.read(8096)
                if not data_flow:
                    break
                md5_value.update(data_flow)
        return md5_value.hexdigest()

    def idle(self, dev, logon=False):
        """
        返回设备开机状态
        """
        result, out = self.adbshell(dev, "getprop dev.bootcomplete", logon)
        return result, out

    def reboot(self, dev, logon=False):
        """
        返回设备开机状态
        """
        result, out = self.adb(dev, "reboot", logon)
        return result, out

    def tryADB(self ,dev,mode ='adb or shell' ,command = 'null', timeout = 30 ,logon = False):
        tryNub = 0
        while True:
            if mode == 'adb':
                result , out = self.adb(dev ,command,logon)
            elif mode == 'shell':
                result, out = self.adbshell(dev, command, logon)
            else:
                logging.error('tryADB mode not is "adb or shell"')
                sys.exit(-1)
            if result == 0:
                return True, out
            else:
                tryNub += 1
                time.sleep(1)
                if tryNub > timeout:
                    logging.warning(out)
                    return False , out

    @staticmethod
    def tryNext(method):
        for x in range(5):
            if method:
                return True
        return False
