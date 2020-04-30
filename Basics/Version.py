# -*- coding: utf-8 -*-

import platform


def Python_version():
    """
    返回python 浮点型版本号
    仅返回大版本号与中版本号，不返回标识号
    例如 python 2.7.15  返回2.7
    """
    f = platform.python_version().split('.')
    return float(r'{0}.{1}'.format(f[0], f[1]))


def OS_version():
    """
    获取操作系统版本号
    """
    f = platform.platform()
    return f


def test():
    print(Python_version())
    print(OS_version())


if __name__ == '__main__':
    test()
