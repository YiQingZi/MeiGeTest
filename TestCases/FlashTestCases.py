# -*- coding: utf-8 -*-

import logging
import sys
import time
from Operation.FlashTest import FlashTest
from Utils.Utils import Utils
from Utils.LogUtils import LogUtils
from Utils.TimeUtils import TimeUtils


class FlashTestRun(FlashTest, LogUtils, Utils, TimeUtils):

    def test_EMMC_pull_and_push(self, dev, testNum):
        testERROR = 0
        result, out = Utils.idle(self, dev, logon=True)
        if result != 0:
            logging.error(out)
            sys.exit(-1)
        Utils.adb(dev, 'root', logon=True)
        for x in range(testNum):
            if not Utils.tryNext(FlashTest._EMMC_push(dev)):
                #break
                testERROR += 1
                LogUtils.logcat_and_dmesg(dev, logon=True)
                time.sleep(10)
                continue
            time.sleep(2)
            if not Utils.tryNext(FlashTest._EMMC_pull(dev)):
                #break
                testERROR += 1
                LogUtils.logcat_and_dmesg(dev, logon=True)
                time.sleep(10)
                continue
            time.sleep(2)
            if not FlashTest.check_md5_isTrue():
                LogUtils.logcat_and_dmesg(dev, logon=True)
                testERROR += 1
            x += 1
            print('第 {0} 次，失败 {1} 次！  {2}\n'.format(str(x), str(testERROR), TimeUtils.strTime()))
            time.sleep(3)
        print('测试结束')