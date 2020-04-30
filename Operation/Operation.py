# -*- coding: utf-8 -*-

from Basics.COMTest import COMTest
from Utils.TimeUtils import TimeUtils
from Basics.TestCasesRead import TestCasesRead


class Test(COMTest, TimeUtils, TestCasesRead):

    def testing(self, com):
        testcases = TestCasesRead.getTestCase(self)
        for case in testcases:
            com_port = COMTest._opencom(com)
            result = COMTest.send_AT_and_Result(self, com_port, case)
            COMTest.close_port(com_port)
            yield '{0} : {1}\n{2}'.format(case, TimeUtils.strTime(), result)

    def testing_write(self, com, str_test):
        com_port = COMTest._opencom(com)
        COMTest._send_AT(com_port, str_test)
        COMTest.close_port(com_port)

    def testing_read(self, com):
        com_port = COMTest._opencom(com)
        while True:
            result = COMTest._wait_Result(com_port)
            if '' != result:
                print(result)