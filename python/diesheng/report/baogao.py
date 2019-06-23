from diesheng.report.HTMLTestReportCN import HTMLTestRunner
import  unittest
def B_gao(name):
    #创建测试套件
    suit=unittest.TestSuite()
#将测试用例添加到测试套件里
#将某一个类中
# suit.addTest(unittest.makeSuite(D_dan))#出现提示语的原因   pycharm本身自带了一个unittest模块
#自动去发现符合通配符的文件中以test开头的函数，提取出来 放在dis列表中
    for  i  in  name:
        dis=unittest.defaultTestLoader.discover(r'E:\PycharmProjects\diesheng\test',pattern='{}.py'.format(i.strip()))
        for j in dis:
            suit.addTest(j)
    f=open('adc.html','wb')
    runner=HTMLTestRunner(stream=f,tester='hyj',description='结果如下',title='别克测试报告')
    runner.run(suit)
    f.close()