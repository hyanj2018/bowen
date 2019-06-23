import unittest
from diesheng.config.shouye import fx
class duanyan(unittest.TestCase):
    def test_1(self):
        b=fx()
        self.assertEqual(b,'审批')
    def test_2(self):
        c=fx()
        self.assertNotIn(c,'日志')
if __name__=='__main__':
    unittest.main()