# -*- coding: utf-8 -*-
import logging

from Utils.Utils import Utils

#测试设备号
#示例：devices = '3a87115'
devices = '1234567'






"""
---------------------------------------------------------------------------
以下不要修改
---------------------------------------------------------------------------
"""

#脚本运行路径
sys_patch = Utils.get_sys_path()

#android内置T卡路径
Tcard_patch = Utils.get_android_Tcard_path(devices)
logging.debug("Tcard_patch :"+str(Tcard_patch))

# android

big = 1073741824 / 1024
# 1G

samplemd5 = 'cd573cfaace07e7949bc0c46028904ff'

Flash_push_EMMC = r'push {0}\Data\sample.zip /sdcard/'.format(sys_patch)
Flash_pull_EMMC = r'pull /sdcard/sample.zip {0}\Data\test'.format(sys_patch)

Flash_push_Tcard = r'push {1}\Data\sample.zip /storage/{0}'.format(Tcard_patch, sys_patch)
Flash_pull_Tcard = r'pull /storage/{0}/sample.zip {1}\Data\test'.format(Tcard_patch, sys_patch)

sample_patch = r'{0}\Data\test\sample.zip'.format(sys_patch)
Del_sample = r"del {0}\Data\test\sample.zip".format(sys_patch)

# appium
