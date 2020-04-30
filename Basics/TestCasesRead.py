# -*- coding: utf-8 -*-

try:
    from Utils.Utils import Utils
except ImportError as err:
    from Utils import Utils


from Basics.Version import Python_version


class TestCasesRead(Utils):
    
    def __readTestCases(self):
        v = Python_version()
        if v > 3.0:
            with open('{0}/testcase.txt'.format(Utils.get_sys_path()), mode='r', encoding='utf-8') as f:
                testcase = f.read()
            return testcase
        else:
            with open('{0}/testcase.txt'.format(Utils.get_sys_path()), mode='r') as f:
                testcase = f.read()
            return testcase
            
    def getTestCase(self):
        testcase = self.__readTestCases()
        caseList = testcase.split('\n')
        return caseList