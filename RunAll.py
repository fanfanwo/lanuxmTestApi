import os,urllib3
import unittest
from common.getfiledir import dir

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class AllTest:
    def __init__(self):
        self.caseListFile = os.path.join(dir, "caselist.txt")
        self.caseFile = os.path.join(dir,"testcase")
        # print(self.caseFile)
        self.caseList = []

    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()
        print(self.caseList)

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)
            # print('suite_module:'+str(suite_module))
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            # print(str(suit))
            if suit is not None:
                print('if-suit')
        except Exception as ex:
            print('err_message:',str(ex))
        finally:
            print("*********TEST END*********")



if __name__ == '__main__':
    AllTest().run()