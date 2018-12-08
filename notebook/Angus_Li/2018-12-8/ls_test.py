#-*- coding: utf-8 -*-
#测试模拟ls命令
import unittest
import mock
import ls
import os
from ddt import ddt,data
from parameterized import parameterized
from unittest.mock import patch

head = "python cmd.py "
@ddt
class TestLs(unittest.TestCase):
    @parameterized.expand([
        ("1st",[],''),
        ("2en",['a','b'],'a b'),
    ])
    def test_dispaly(self,name,test_list,expect):
        with patch("builtins.print") as mocked_print:
            ls.display(test_list)
            mocked_print.assert_called_with(expect)

    @parameterized.expand([
        ("1st",'/home/liyongjie/',32504)
        ("2en",'/home/liyongjie/Mona',8)
    ])
    def test_total_returnIntTotal(self,name,path,expected):
        dir_list = os.listdir(path)
        total = ls.deal_total(dir_list)
        self.assertEqual(total,expected)

    @parameterized.expand([
        ("1st",1541686475.5541823,'11月 8 22:14')
        ("2en",1523452205.648194,'4月  18  2018')
    ])
    def test_deal_time_returnStringTime(self,name,origin_time,str_fmt_time):
        fmt_time = ls.deal_time(origin_time)
        self.assertEqual(fmt_time,str_fmt_time)

    @parameterized.expand([
        ("1st",'/home/liyongjie/temp','100/n ---------- 1 liyongjie liyongjie 0 0000000 a.txt')
        ("2en",'/home/liyongjie/Mona',('100/n'
            '---------- 4 liyongjie liyongjie 4096 0000000 notebook'
            '---------- 1 liyongjie liyongjie  790 0000000 README.md'))
    ])
    def test_ls_option_l(self,name,path,expected):
        ls.file_list = os.listdir(path)
        deal_total = mock.Mock(return_value='100')
        deal_time = mock.Mock(return_return_value='0000000')
        class_chmod_fmt = mock.Mock(return_value='----------')
        with patch("builtins.print") as mocked_print:
            ls.ls_option_l()
            mocked_print.assert_called_with(expected)

    @data('ls','ls -la','Ls','ls -l -a','ls -l Mona git',)
    def test_ls(self,value):
        python_list = os.system(head + value)
        linux_ls = os.system(value)
        print(python_list)
        with patch("builtins.print") as mocked_print:
            print(python_list)
            mocked_print.assert_called_with(linux_ls)

if __name__ == '__main__':
    unittest.main()




        


