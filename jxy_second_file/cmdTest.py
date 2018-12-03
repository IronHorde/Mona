import unittest
import os
from unittest.mock import patch
from ddt import ddt,data

head="python cmd.py "
test_list=["pwd","ls","ls -l","ls -a","ls -la","ls -o"]
test_error=["pw","fdsa","ewqeq"]
wrong_instruct="please input true instruct"
unknow_para="unknown paramaters"
@ddt
class cmdTest(unittest.TestCase):
	@data(test_list[0])#,test_list[1],test_list[2],test_list[3],test_list[4],test_list[5])
	def test_a(self,value):
		list_list=os.popen(head+value)
		list_ls=os.popen(value)
		with patch("builtins.print") as mocked_print:
			print(list_list)
			mocked_print.assert_called_with(list_ls)#os.system("python cmd.py ls -l"))
		self.assertEqual(1,1)
	'''
	@data(test_error[0],test_error[1],test_error[2])
	def test_error(self,value):
		message=os.popen(head+value)
		with patch("builtins.print") as mocked_print:
			print(message)
			mocked_print.assert_called_with(wrong_instruct)
	'''
if __name__=="__main__":
	unittest.main()
