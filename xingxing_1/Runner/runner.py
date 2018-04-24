#coding=utf-8
import unittest, os, time
from Common import HTMLTestRunner

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
casepath = PATH("../TestCase/")
discover = unittest.defaultTestLoader.discover(casepath, pattern="test*.py")
now = time.strftime("%Y%m%d_%H-%M-%S", time.localtime(time.time()))
htmlpath = PATH("../Report/report_%s.html" % now)
fp = open(htmlpath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="自动化测试报告", description="测试内容")
runner.run(discover)








