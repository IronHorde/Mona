import os
import sys
import pwd
import grp
import time

instruct={"pwd":1,"ls":2,"exit":3}
chmod_value={0:"---",1:"--x",2:"-w-",3:"-wx",4:"r--",5:"r-x",6:"rw-",7:"rwx"}
month_value=('Jan','Feb','Mar','Apr','May','Jun')
ls_value=('l','a','o')

def removeHidenFile(file_list):
	result=[]
	for i in range(0,len(file_list)):
		if not file_list[i].startswith("."):
			result.append(file_list[i])
	return result

def pwd_instruct(input_size):
	if input_size > 2:
		print("unknown parameters")
		return
	print(os.getcwd())
	return

def ls(input_size):
	if input_size > 3:
		print("unknown parameters")
		return
	elif input_size == 2:
		file_list=os.listdir()
		file_list=removeHidenFile(file_list)
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
			file_list=getFileList(False)
		else:
			file_list=getFileList(True)
		#output file info
		output_list=getFileListInfo(os.getcwd(),file_list,para)
		for i in range(0,len(output_list)):
			print(output_list[i])

		'''
		ls_num=ls_value[sys.argv[2]]
		if ls_num == 1:
			output_list=[]
			file_list=getFileList(True)
			output_list=getFileListInfo(os.getcwd(),file_list)
			for i in range(0,len(output_list)):
				print(output_list[i])			
		elif ls_num == 2:
			file_list=getFileList(False)
			for i in range(0,len(file_list)):
				print(file_list[i])
		elif ls_num == 3:
			output_list=[]
			file_list=getFileList(False)
			output_list=getFileListInfo(os.getcwd(),file_list)
			for i in range(0,len(output_list)):
				print(output_list[i])
		'''
			

def getFileList(flag):
	file_list=os.listdir()
	result=[]
	if flag:
		result=removeHidenFile(file_list)
	else:
		file_list.insert(0,"..")
		file_list.insert(0,".")
		result=file_list
	return result


def getFileListInfo(path,file_list,para):
	output_list=[]
	if "l" in para:
		totel=0
		for i in range(0,len(file_list)):
			if not os.path.isdir(file_list[i]):
				totel+=(int(os.path.getsize(file_list[i])/4096)+1)
			'''
			else:
				totel+=1
			'''
			output_list.append(getFileInformation(os.getcwd(),file_list[i],para))
		output_list.insert(0,"totel:"+str(totel*4))
	else:
		output_list=file_list		
	return output_list


def getFileInformation(path,filename,para):
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
	os_info=os.stat(filename)
	info+=". "+str(os_info.st_nlink)
	complete_time=time.ctime(os_info.st_mtime)
	
	time_value=complete_time.split()
	time_real=""
	if time_value[1] not in month_value:
		time_real=time_value[1]+" "+time_value[2]+" "+":".join(time_value[3].split(":")[0:2])
	else:
		time_real=time_value[1]+" "+time_value[2]+" "+time_value[4]
	if "o" not in para:
		info=info+" "+pwd.getpwuid(os_info.st_uid)[0]+" "+\
			grp.getgrgid(os_info.st_gid)[0]+" "+str(os_info.st_size)+" "+\
				time_real+" "+filename
	else:
		info=info+" "+str(os_info.st_size)+" "+time_real+" "+filename
	return info
		


def main():
	input_size=len(sys.argv)
	if input_size==1:
		print("please input true instruct")
		return
	if sys.argv[1] not in instruct:
		print("please input true instruct")
		return
	ins=instruct[sys.argv[1]]
	if ins==1:
		pwd_instruct(input_size)
	elif ins==2:
		ls(input_size)

def add(a,b):
	return a+b

if __name__=="__main__":
	main()
