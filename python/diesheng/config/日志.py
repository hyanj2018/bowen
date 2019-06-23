#python自带的写日志模块
#日期模块
import logging
import datetime
import os
#第一步创建一个日志文件
log_file = os.path.join(r'E:\PycharmProjects\diesheng\log',str(datetime.datetime.now().date())+'.out')

#第二部定义一个日志文件输出格式:时间，脚本的名字，代码执行的行号
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
                              datefmt='%d-%m-%Y:%H:%M:%S')

#第三步：将日志以字节流的形式输出，输出到控制台
con_handler = logging.StreamHandler()
#第四步：将日志输出到日志文件内
fil_handler = logging.FileHandler(log_file,encoding='utf-8')
#第五步：给输出到控制台的日志添加格式
con_handler.setFormatter(formatter)
#第六步给输出到的文件的日志添加格式
fil_handler.setFormatter(formatter)
#定义一个日志函数，供别的脚本使用
def get_logger(name):
    """

    :param name: 脚本的名字，例如：在test_1.py使用get_logger,name==test_1
    :return:
    """
    logger = logging.getLogger(name)
    logger.addHandler(con_handler)
    logger.addHandler(fil_handler)
    logger.setLevel(logging.INFO)
    return logger
