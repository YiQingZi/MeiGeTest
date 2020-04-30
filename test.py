# -*- coding: utf-8 -*-
import logging


from TestCases.FlashTestCases import FlashTestRun
from Utils.LogUtils import LogUtils
from Config.TestConfig import devices

"""
def main():
    print('\n')
    test1 = Test()
    result = test1.testing('com254')
    for re in result:
        print(re)
        print('-------------------------------------------------------')
"""

if __name__ == '__main__':
    logging.debug('test running')
    '''
    test = Test()
    while True:
        result = test.testing_write('COM195' , 'ff')
        time.sleep(2)
    '''
    # main()
    test = FlashTestRun()
    test.test_EMMC_pull_and_push(devices, 2)
    LogUtils.com_log('com195')
    # log.logcat_and_dmesg(dev ='62b72966', logon =True)
