# -*- coding: utf-8 -*-

import logging
import subprocess
import re
import sys
from Basics.Version import Python_version


def run_command(command='NO_COMMAND_GIVEN', logon=False):
    """
    执行命令行，兼容2.x 与 3.x版本
    执行成功返回执行结果，否则为空
    """
    logging.debug("RUN: '{0}'".format(command))
    version = Python_version()
    if version == 2.7:
        P = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        out = P.communicate()[0]
        out = re.sub(r"\r+\n", r'\n', out)
        logging.debug("Command '{0}' output: '{1}'".format(command, out))
        result = P.wait()
        if result == 0:
            return result, out
        else:
            if logon:
                logging.warning("Command '{0}' failed to run, output:{1}".format(command, out))
    if version > 3.3:
        try:
            P = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True, encoding='utf-8',
                               shell=True)
            out = P.stdout
            out = re.sub(r'\r+\n', r'\n', out)
            logging.debug("Command '{0}' output: '{1}'".format(command, out))
            return 0, out
        except subprocess.CalledProcessError as error:
            result = error.returncode
            out = error.output
            if logon:
                logging.warning("RUN: '{0}'".format(out))
    else:
        logging.error('Python_version is {0} < 3.3 , sys exit, please update python'.format(version))
        sys.exit(-1)
    return result, out


def test():
    run_command('adb devices', True)
    run_command('adb devices1', True)


if __name__ == '__main__':
    test()
