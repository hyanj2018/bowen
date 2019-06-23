from diesheng.test.断言 import duanyan
from HTMLTestReportCN import HTMLTestRunner

import unittest
def baogao(*x):
    suit=unittest.TestSuite()
    for i in x:
        suit.addTest(duanyan(i))
    f=open(r'E:\PycharmProjects\diesheng\report\c.html','wb')
    runner=HTMLTestRunner(stream=f,tester='hyj',description='结果如下',title='搜索跳转',verbosity=2)
    runner.run(suit)
# baogao('test_1','test_2')