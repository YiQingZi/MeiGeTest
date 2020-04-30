# -*- coding: utf-8 -*-


from Config.TestConfig import *


class FlashTest(Utils):#TimeUtils , LogUtils
    
    @staticmethod
    def _EMMC_push(device):
        result, out = Utils.adb(device, Flash_push_EMMC, logon=True)
        if result == 0:
            out = out.replace('\n', '')
            print(out)
            return True
        else:
            logging.error(out)
            return False
            
    @staticmethod
    def _EMMC_pull(device):
        result, out = Utils.adb(device, Flash_pull_EMMC, logon=True)
        if result == 0:
            out = out.replace('\n', '')
            print(out)
            return True
        else:
            logging.error(out)
            return False
            
    @staticmethod
    def _Tcard_push(device):
        result, out = Utils.adb(device, Flash_push_Tcard, logon=True)
        if result == 0:
            out = out.replace('\n', '')
            print(out)
            return True
        else:
            logging.error(out)
            return False
            
    @staticmethod
    def _Tcard_pull(device):
        result, out = Utils.adb(device, Flash_pull_Tcard, logon=True)
        if result == 0:
            out = out.replace('\n', '')
            print(out)
            return True
        else:
            logging.error(out)
            return False

    @staticmethod
    def check_md5_isTrue():
        try:
            md = Utils.md5_calc(sample_patch)
        except IOError as err:
            logging.error(err)
            md = '0'
        if md in samplemd5:
            return True
        else:
            return False