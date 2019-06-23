# from  HTMLTestReportCN import  HTMLTestRunner
# import  unittest
# from  appium  import  webdriver
# from  time  import  sleep
# import  warnings
# des = {
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.qk.butterfly",
#     "appActivity": ".main.LauncherActivity",
#     "noReset": "true",
# }
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# sleep(10)
# dr.find_element_by_id("com.qk.butterfly:id/v_login_pwd").click()
# sleep(2)
# dr.find_element_by_id("com.qk.butterfly:id/et_login_phone").send_keys("19937102621")
# sleep(2)
# dr.find_element_by_id("com.qk.butterfly:id/et_login_pwd").send_keys("jie2121")
# sleep(2)
# dr.find_element_by_id("com.qk.butterfly:id/tv_to_login").click()
# sleep(2)
# dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.RelativeLayout")[-1].click()
# sleep(2)
# dr.find_element_by_id("com.qk.butterfly:id/v_me_setting").click()
# sleep(3)
# dr.find_element_by_id("com.qk.butterfly:id/v_me_grade").click()
# sleep(4)
# dr.find_element_by_id("com.qk.butterfly:id/tv_ok").click()


import  unittest
from  appium  import  webdriver
from  time  import  sleep
from  diesheng.config import  config_1
from  diesheng.config import  config_2
from  diesheng.config.config_3 import get_logger
log = get_logger("config_4")
class  DS(unittest.TestCase):
    def setUp(self):
        self.des = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.tim",
            "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
            "noReset": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true"
        }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(10)
        log.info("手机与appium服务器建立连接成功.....")
    def  config_4(self):
        log.info("点击密码按键，进入账号密码登录页面")
        self.dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").clear()
        sleep(4)
        for i in  config_1.read_data():
            self.dr.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱").send_keys(i[0])
            sleep(2)
            log.info(f"输入的手机号是：{i[0]}")
            self.dr.find_element_by_id("com.tencent.tim:id/password").send_keys(i[1])
            sleep(2)
            log.info(f"输入的手机号是：{i[1]}")
            self.dr.find_element_by_id("com.tencent.tim:id/login").click()
            log.info("点击登录按钮")
            sleep(6)
            """
            if  else 处理登录成功与失败，也可以使用try except语句做断言

            """
            try:
                log.info("登录失败的处理......")
                b = self.dr.find_element_by_id("com.qk.butterfly:id/tv_to_login").text
                print("登录失败")
                self.assertEqual(b,"登录",msg="登录失败")
            except:
                log.info("登录成功的处理......")
                a =  self.dr.find_elements_by_id("com.qk.butterfly:id/tv_tab")[-1].text
                self.assertEqual(a,"首页",msg="断言已经登录成功")
    def tearDown(self):
        log.info("手机与appium断开连接......")
        self.dr.quit()
if __name__=='__main__':
    # unittest.main()
    config_2.report(test_name=DS("config_4"),report_path=r"E:\PycharmProjects\diesheng\report\a.html")