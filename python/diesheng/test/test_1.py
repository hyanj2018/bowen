#导入模块
# from  HTMLTestReportCN import  HTMLTestRunner
# import  unittest
# from  appium  import  webdriver
# from  time  import  sleep
# class  DS(unittest.TestCase):
# #     #每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
# #     def setUp(self):
# #         self.des = {
# #             "platformName": "Android",
# #             "platformVersion": "5.1.1",
# #             "deviceName": "emulator-5554",
# #             "appPackage": "com.qk.butterfly",
# #             "appActivity": ".main.LauncherActivity",
# #             "noReset": "true",
# #         }
# #         # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
# #         # 测试脚本与appium服务器建立一个session连接
# #         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
# #         sleep(10)
#     #写测试用例的部分
#     def  test_1(self):
#         #使用账号密码登录碟声
#         #点击密码，进入手机号，密码登录页面
#         self.dr.find_element_by_id("com.qk.butterfly:id/v_login_pwd").click()
#         sleep(2)
#         #进入账号密码登录页面之后
#         self.dr.find_element_by_id("com.qk.butterfly:id/et_login_phone").send_keys("19937102621")
#         sleep(2)
#         self.dr.find_element_by_id("com.qk.butterfly:id/et_login_pwd").send_keys("jie2121")
#         sleep(2)
#         self.dr.find_element_by_id("com.qk.butterfly:id/tv_to_login").click()
#
#         #断言
#         sleep(6)
#         #进入登录之后的页面
#         a =  self.dr.find_elements_by_id("com.qk.butterfly:id/tv_tab")[-1].text
#         self.assertEqual(a,"首页",msg="断言已经登录成功")
#     #每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境残留数据
#     def tearDown(self):
#         self.dr.quit()
# if __name__=='__main__':
#     unittest.main()
#     sleep(6)


import  unittest
from  appium  import  webdriver
from  time  import  sleep
from  diesheng.config import  config_1
from  diesheng.config import  config_2
#导入封装好的日志函数
from  diesheng.config.config_3 import get_logger
#创建变量接受日志的句柄 ---> 一根笔
log = get_logger("test_1")
#testCase 写测试用例的类，单元测试必须继承于unittest.TestCase
class  DS(unittest.TestCase):
    # """"""
    #   def __init__(self): 初始化函数，传递参数，自动运行
    # """"""
    #每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):  #相当于init方法，类被调用的时候，会自动运行
        self.des = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "true",
        }
        # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
        # 测试脚本与appium服务器建立一个session连接
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(10)
        log.info("手机与appium服务器建立连接成功.....")
    #写测试用例的部分
    def  test_1(self):  
        # 使用账号密码登录碟声
        # 点击密码，进入手机号，密码登录页面
        log.info("点击密码按键，进入账号密码登录页面")
        self.dr.find_element_by_id("com.qk.butterfly:id/v_login_pwd").click()
        sleep(2)
        #使用脚本与测试数据相结合
        for i in  config_1.read_data():
        #进入账号密码登录页面之后
            self.dr.find_element_by_id("com.qk.butterfly:id/et_login_phone").send_keys(i[0])
            sleep(2)
            log.info(f"输入的手机号是：{i[0]}")
            self.dr.find_element_by_id("com.qk.butterfly:id/et_login_pwd").send_keys(i[1])
            sleep(2)
            log.info(f"输入的手机号是：{i[1]}")
            self.dr.find_element_by_id("com.qk.butterfly:id/tv_to_login").click()
            log.info("点击登录按钮")
            #断言
            sleep(6)
            """
            if  else 处理登录成功与失败，也可以使用try except语句做断言

            """
            try:
                log.info("登录失败的处理......")
                b = self.dr.find_element_by_id("com.qk.butterfly:id/tv_to_login").text
                print("登录失败")
                self.assertEqual(b,"登录",msg="登录失败")
                # if b == "登录":
                #     print("登录失败")
            except:
                #进入登录之后的页面
                log.info("登录成功的处理......")
                a =  self.dr.find_elements_by_id("com.qk.butterfly:id/tv_tab")[-1].text
                self.assertEqual(a,"首页",msg="断言已经登录成功")
    #每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境残留数据
    def tearDown(self):
        log.info("手机与appium断开连接......")
        self.dr.quit()
if __name__=='__main__':
    unittest.main()
    config_2.report(test_name=DS("test_1"),report_path=r"E:\PycharmProjects\diesheng\report\a.html")