import os
import sys
import pwd
import grp
import time

instruct={"pwd":1,"ls":2,"exit":3}
chmod_value={0:"---",1:"--x",2:"-w-",3:"-wx",4:"r--",5:"r-x",6:"rw-",7:"rwx"}
month_value={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
ls_value=('l','a','o')

def remove_hiden_file(file_list):
    '''This method will delete hiden file name from file_list because 'ls -l ' will not show hiden file'''
    result=[]
    for i in range(0,len(file_list)):
        if not file_list[i].startswith("."):
            result.append(file_list[i])
    return result

def pwd_instruct(input_size):
    '''This is 'pwd' method which can show your workstation,it has no parameter,'os.getcwd' support this method '''
    if input_size > 2:
        print("unknown parameters")
        return
    print(os.getcwd())
    return

def ls(input_size):
    '''
    This method can show your file message in this dir,it has one parameter,it rely on "os,pwd,grp,time" and other methods in this file 
    parameters format must be "-xxx"'''
    if input_size > 3:
        print("unknown instruct")
        return
    elif input_size == 2:
        file_list=os.listdir()
        file_list=remove_hiden_file(file_list)
        for i in range(0,len(file_list)):
            print(file_list[i])
        return
    else:
        if not sys.argv[2].startswith("-"):
            print("unknown parameters")
            return
        para=[]
        if len(sys.argv[2]) >= 2:
            for i in range(1,len(sys.argv[2])):
                if sys.argv[2][i] not in ls_value:
                    print("unknown parameters")
                    return
                para.append(sys.argv[2][i])
        else:
            print("unknown parameters")
            return
        output_list=[]
        file_list=[]
        #get file list
        if "a" in para:
            file_list=get_file_list(False)
        else:
            file_list=get_file_list(True)
        #output file info
        output_list=get_file_list_info(os.getcwd(),file_list,para)
        for i in range(0,len(output_list)):
            print(output_list[i])	

def get_file_list(flag):
    '''this method aim to make sure the file name list user want to see '''
    file_list=os.listdir()
    result=[]
    if flag:
        file_list=remove_hiden_file(file_list)
    else:
        file_list.insert(0,"..")
        file_list.insert(0,".")
    result=file_list
    result.sort()
    return result

def get_file_list_info(path,file_list,para):
    '''"ls -l" will show the file's details ,this method aim to imitation it '''
    output_list=[]
    if "l" in para:
        totel=0
        for i in range(0,len(file_list)):
            if not os.path.isdir(file_list[i]):
                totel+=(int(os.path.getsize(file_list[i])/4096)+1)
            output_list.append(get_file_information(os.getcwd(),file_list[i],para))
        output_list.insert(0,"totel:"+str(totel*4))
    else:
        output_list=file_list		
    return output_list

def get_file_type_and_chmod(path,filename):
    '''get file's chmod and show it with "rwx" ,it also can be shown like "777" by modify'''
    info=""
    if os.path.isdir(filename):
        info+="d"
    elif os.path.isfile(filename):
        info+="-"
    elif os.path.islink(filename):
        info+="l"
    chmod=oct(os.stat(filename).st_mode)[3:]
    for i in range(0,len(chmod)):
        if chmod[i] != '0':
            info+=chmod_value[int(chmod[i])]
    return info+"."

def get_link_num(os_info):
    '''get how many links to this file,work by "st_nLink"'''
    return str(os_info.st_nlink)

def get_file_date(os_info):
    complete_time=time.ctime(os_info.st_mtime)
    localtime=time.localtime(time.time())
    time_value=complete_time.split()
    time_real=""
    if abs(month_value[time_value[1]]-int(localtime.tm_mon)) <= 6:
        time_real=time_value[1]+" "+time_value[2]+" "+":".join(time_value[3].split(":")[0:2])
    else:
        time_real=time_value[1]+" "+time_value[2]+" "+time_value[4]
    return time_real

def get_user_and_group_id(os_info,type):
    '''get user name and group name'''
    if type == 1:
        return str(os_info.st_uid)+" "+str(os_info.st_gid)
    elif type == 2:
        return pwd.getpwuid(os_info.st_uid)[0]+" "+grp.getgrgid(os_info.st_gid)[0]
    else:
        return ""

def get_file_size(os_info):
    return str(os_info.st_size)

def get_inode(os_info):
    return str(os_info.st_ino)

def get_file_information(path,filename,para):
    '''to get details for each files'''
    type=0
    info=""
    info+=get_file_type_and_chmod(path,filename)
    os_info=os.stat(filename)
    info=info+" "+get_link_num(os_info)
	
    if "o" not in para:
        type = 2
    info=info+" "+get_user_and_group_id(os_info,type)
    info=info+" "+get_file_size(os_info)
    info=info+" "+get_file_date(os_info)
    info=info+" "+filename
    return info

def main():
    input_size=len(sys.argv)
    if input_size==1:
        print("unknown instruct")
        return
    if sys.argv[1] not in instruct:
        print("unknown instruct")
        return
    ins=instruct[sys.argv[1]]
    if ins==1:
        pwd_instruct(input_size)
    elif ins==2:
        ls(input_size)

if __name__=="__main__":
    main()
