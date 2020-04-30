# -*- coding: utf-8 -*-

from Basics.Version import Python_version
import sys
import logging

v = Python_version()

if v >= 3.4:
    try:
        import serial
    except ImportError as err:
        logging.error(err)
        sys.exit(-1)
else:
    logging.error('AT test (serial) need python_version >= 3.4 ,but the current version = {0}'.format(str(v)))


class COMTest:
    """
    串口测试基类
    """
    # 打开串口函数
    @staticmethod
    def _opencom(com, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1):
        """
        打开串口
        """
        try:
            com_port = serial.Serial(com, baudrate, bytesize, parity, stopbits, timeout)
            return com_port
        except (serial.SerialException, ValueError) as error:
            logging.error(error)
            sys.exit(-1)

    # 关闭串口，释放资源
    @staticmethod
    def close_port(com_port):
        com_port.close()
        return None

    # 发送指令
    @staticmethod
    def _send_AT(com_port, strAT='ATE'):
        try:
            com_port.write(strAT.encode('utf-8') + b'\r')
            return True
        except serial.SerialTimeoutException as error:
            logging.error(error)
            return False

    # 等待AT返回值
    @staticmethod
    def _wait_AT_Result(com_port, strAT):  # AT+SGSW
        result = ''
        while True:
            line = com_port.readline()
            result = result + line.decode('utf-8', 'replace')
            if strAT in result:
                result = ''
            if 'OK' in result:
                break
            if 'ERROR' in result:
                break
            if line == b'':
                break
        return result

    # 获取串口结果
    @staticmethod
    def _wait_Result(com_port):  # AT+SGSW
        result = ''
        line = com_port.readline()
        result = result + line.decode('utf-8', 'replace')
        return result

    # 发送指令并获取返回值
    def send_AT_and_Result(self, com_port, strAT='ATE'):
        if self._send_AT(com_port, strAT):
            result = self._wait_AT_Result(com_port, strAT)
            logging.debug('send :{0} ,output:{1}'.format(strAT, result))
            return result
        else:
            return 'SEND AT TIME OUT'
