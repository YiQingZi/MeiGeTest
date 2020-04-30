# -*- coding: utf-8 -*-


from Basics.Version import Python_version
from Basics.COMTest import COMTest
from Utils.Utils import Utils
from Utils.TimeUtils import TimeUtils
import re


class LogUtils(Utils, TimeUtils, COMTest):

    @staticmethod
    def logcat(dev='Null', logname=None, logon=False):
        """
        logcat log
        """
        result, out = Utils.adbshell(dev, "logcat -d -v time", logon)
        if logname is None:
            logname = '{0}/log/{1}-{2}-logcat.log'.format(Utils.get_sys_path(), dev, TimeUtils.strTimeName())
        if result == 0:
            v = Python_version()
            if v > 3.0:
                Utils.saveTxtFile(logname, data=out)
            else:
                Utils.saveTxtFile(logname, data=out)
        return result, out

    @staticmethod
    def dmesg(dev='Null', logname=None, logon=False):
        """
        dmesg log
        """
        result, out = Utils.adbshell(dev, "dmesg", logon)
        if logname is None:
            logname = '{0}/log/{1}-{2}-dmesg.log'.format(Utils.get_sys_path(), dev, TimeUtils.strTimeName())
        if result == 0:
            v = Python_version()
            if v > 3.0:
                Utils.saveTxtFile(logname, data=out)
            else:
                Utils.saveTxtFile(logname, data=out)
        return result, out

    @staticmethod
    def logcat_and_dmesg(dev='Null', logname=None, logon=False):
        """
        logcat  和  dmesg log
        """
        if logname is None:
            logname = '{0}/log/{1}-{2}'.format(Utils.get_sys_path(), dev, TimeUtils.strTimeName())
        result_dmesg, out_dmesg = Utils.adbshell(dev, "dmesg", logon)
        result_logcat, out_logcat = Utils.adbshell(dev, "logcat -d -v time", logon)
        if result_dmesg == 0:
            Utils.saveTxtFile('{0}-dmesg.log'.format(logname), data=out_dmesg)
        if result_logcat == 0:
            Utils.saveTxtFile('{0}-logcat.log'.format(logname), data=out_logcat)
        return result_dmesg, out_dmesg, result_logcat, out_logcat

    @staticmethod
    def com_log(com, dev='Null', logname=None):
        """
        串口log
        """
        com_port = COMTest._opencom(com)
        if logname is None:
            logname = '{0}/log/{1}-{2}'.format(Utils.get_sys_path(), dev, TimeUtils.strTimeName())
        while True:
            result = COMTest._wait_Result(com_port)
            v = Python_version()
            if v > 3.0:
                print(result, end='')
            else:
                print(result),
            result = re.sub(r'\n', '', result)
            logname_new = '{0}-com_log.log'.format(logname)
            size = Utils.get_FileSize(logname_new)
            if size > 2.00:
                logname = '{0}/log/{1}-{2}'.format(Utils.get_sys_path(), dev, TimeUtils.strTimeName())
                logname_new = '{0}-com_log.log'.format(logname)
            Utils.saveTxtFile(logname_new, data=result)
