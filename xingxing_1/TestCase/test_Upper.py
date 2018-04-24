#coding=utf-8
import unittest

class UpperTest(unittest.TestCase):
    '''测试字符串大写'''
    def setUp(self):
        self.teststr = "hello world!"

    def testUpper(self):
        '''字符串大写'''
        uper = self.teststr.upper()
        self.assertEqual(uper, self.teststr)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()



