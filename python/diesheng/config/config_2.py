from diesheng.report.HTMLTestReportCN import HTMLTestRunner
import  unittest
def report(test_name,report_path):
# 第一步：创一个测试套件，理解成玩具枪的弹夹
    suite = unittest.TestSuite()
#     #第二步：向测试套件里面添加测试用例，理解成玩具枪的bb弹（子弹）
    suite.addTest(test_name)
#     #第三步：将生成的测试结果写入html文件里，理解成玩具枪上膛
    with  open(report_path,'wb')  as  fb:
        runner = HTMLTestRunner(
            stream = fb,
            title = '报告名称',
            description = '报告的描述信息',
            verbosity = 2,
#             #输出内容的详细等级，默认是0,2代表最详细
        )
#         #执行测试用例，并生成HTML测试报告，理解成玩具枪发射子弹
        runner.run(suite)