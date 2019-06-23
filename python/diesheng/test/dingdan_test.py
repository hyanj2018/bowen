from diesheng.config.dingdan import Ding_Dan
from  diesheng.data.dingdan_duqu  import  shuju
import unittest
class D_dan(unittest.TestCase):
    ss = shuju()
    print(ss)
    def test_1(self):
        aaa = Ding_Dan().Cha_mingxi(int(self.ss[1][0]))
        self.assertEqual(aaa['errMsg'],"处理成功")
    def test_2(self):
        aaa = Ding_Dan().Cha_mingxi(self.ss[2][0])
        self.assertNotIn("处理成功",aaa)
if __name__=="__main__":
    #自动去检测继承了TestCase类的类中所有所有以test开头的函数
    #将所有的以test开头的函数当成测试用例
    #执行顺序是按照test后的字符在ascii中的位置排序来执行
    unittest.main()