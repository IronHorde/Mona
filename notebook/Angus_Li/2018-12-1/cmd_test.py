import unittest
import os
from unittest.mock import patch
from ddt import ddt,data

head = "python cmd.py "
@ddt
class cmd_test(unittest.TestCase):
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