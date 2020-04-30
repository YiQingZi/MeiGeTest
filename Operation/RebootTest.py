import logging
import time

from Utils.LogUtils import LogUtils
from Utils.TimeUtils import TimeUtils
from Config.TestConfig import *


class RebootTest(LogUtils, Utils, TimeUtils):


    def reboot(self, testNub=0, **kwargs):
        testERR = 0
        test = 0
        tryNext = 0
        while True:
            result, out = Utils.idle(self, devices, logon=False)
            if result == 0 and '1' in out:
                test += 1
                print('test times:{0} ,device {1} reboot up at {2}'.format(str(test), devices , TimeUtils.strTime()))
                Utils.tryADB(self, devices, mode='adb', command='root', timeout=30)
                Utils.tryADB(self,devices,mode= 'shell',command=adb_reboot,timeout=30)
                time.sleep(15)
            else:
                time.sleep(3)
                tryNext += 1
                if tryNext > 100:
                    testERR += 1
                    LogUtils.logcat(devices)
                    logging.warning('wait to test device UI UP and time out (300s)')
                    break
            test = testERR + test
            if test == testNub:
                print('test end')
                break