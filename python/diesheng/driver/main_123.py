#driver 中主要是控制跑回归测试时只跑哪些模块的用例
import xlrd
from diesheng.report.baogao import B_gao
with  open(r'E:\PycharmProjects\diesheng\driver\b.txt','r') as  f:
    a = f.readlines()
    print(a)
    if 'all' in a:
        B_gao('*')
    else:
        B_gao(a)

