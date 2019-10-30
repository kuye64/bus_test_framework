# coding = utf-8
import unittest
from testsuites import test_bus_search

suite = unittest.TestLoader().discover("testsuites")


if __name__=='__main__':
    #执行用例
    runner = unittest.TextTestRunner()
   # runner.addTest(test_bus_search(""))
    runner.run(suite)