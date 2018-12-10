import unittest
import os
from unittest.mock import patch
from ddt import ddt,data
import cmd as cmd_jxy

head="python cmd.py "
test_list=["pwd","ls","ls -l","ls -a","ls -la","ls -o"]
instruct_error=["","pw","fdsa","ewqeq"]
paramaters_error=["pwd -x","ls -m","ls a","ls -lm","ls -","ls -a -p"]
wrong_instruct="unknown instruct"
unknow_para="unknown paramaters"
file_list=["a.txt","b.txt",".c.txt"]
class mockOs():
    def __init__(self,st_uid,st_gid):
        self.st_uid=st_uid
        self.st_gid=st_gid
@ddt
class cmdTest(unittest.TestCase):
    def test_remove_hiden_file_return_list(self):
        result=cmd_jxy.remove_hiden_file(file_list)
        self.assertNotIn(".c.txt",result)

    @data(("ls",True),("ls -a",False))
    def test_get_file_list(self,value):
        list=cmd_jxy.get_file_list(value[1])
        result=os.popen(value[0])
        with patch("builtins.print") as mocked_print:
            print(list)
            mocked_print.assert_called_with(result)

    def test_get_file_list_info_return_output_list(self):
        dir_bool=unittest.mock.Mock(return_value=False)
        file_size=unittest.mock.Mock(return_value=4096)
        info_str=unittest.mock.Mock(return_value="aaa")
        with patch("os.path.isdir",dir_bool):
            with patch("os.path.getsize",file_size):
                with unittest.mock.patch("cmd.get_file_information",info_str):
                    result=cmd_jxy.get_file_list_info("",file_list,"l")
                    self.assertEqual(result[0],"totel:24")

    @data((0,""),(1,"0 0"),(2,"root root"))
    def test_get_user_and_group_id_return_name_or_id(self,value):
        st_info=mockOs(0,0)
        '''
        st_info.st_uid=mock.Mock(return_value=0)
        st_info.st_gid=mock.Mock(return_value=0)
        '''
        result=cmd_jxy.get_user_and_group_id(st_info,value[0])
        self.assertEqual(value[1],result)

    @data(test_list[0])#,test_list[1],test_list[2],test_list[3],test_list[4],test_list[5])
    def test_main_right_instruct_printResultAsLinuxSystem(self,value):
        list_list=os.popen(head+value)
        list_ls=os.popen(value)
        with patch("builtins.print") as mocked_print:
            print(list_list)
            mocked_print.assert_called_with(list_ls)#os.system("python cmd.py ls -l"))

    @data(instruct_error[0],instruct_error[1],instruct_error[2],instruct_error[3])
    def test_main_instructError_returnErrorMessage(self,value):
        message=os.popen(head+value)
        with patch("builtins.print") as mocked_print:
            print(message)
            mocked_print.assert_called_with(wrong_instruct)
	
    @data(paramaters_error[0],paramaters_error[1],paramaters_error[2],paramaters_error[3],paramaters_error[4],paramaters_error[5])
    def test_main_paramError_returnErrorMessage(self,value):
        message=os.popen(head+value)
        with patch("builtins.print") as mocked_print:
            print(message)
            mocked_print.assert_called_with(unknow_para)
		
if __name__=="__main__":
    unittest.main()
