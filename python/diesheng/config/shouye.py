from  selenium  import  webdriver
from  time  import  sleep
from diesheng.config.日志 import get_logger
log=get_logger(name='test_1')
def fx():
    dr = webdriver.Firefox()
    dr.get('https://fxiaoke.com')
    sleep(3)
    dr.find_element_by_xpath('/html/body/header/div/div/div[5]/a[1]').click()
    log.info("登录")
    sleep(3)
    aa=dr.window_handles
    dr.switch_to.window(aa[-1])
    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/ul/li[2]').click()
    log.info("切换账号密码登录")
    sleep(3)
    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/input').send_keys('13014623984')
    log.info("输入密码")
    sleep(3)
    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/input').send_keys('1234qwer')
    log.info("输入账号")
    sleep(3)
    dr.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div/div[6]').click()
    log.info("点击登录")
    sleep(10)

    a=dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/ul/li[3]/a').text
    return a

# fx()