import sys,os,stat,pwd,datetime
from dateutil.relativedelta import relativedelta

#权限格式化(七种文件加格式化权限)
def class_chomd_fmt(class_chomd):
    cla = class_chomd[:-3]
    chomd = class_chomd[-3:]
    result = ''
    if cla=="140":result+='s'
    elif cla=="120":result+='l'
    elif cla=="100":result+='-'
    elif cla=="60":result+='b'
    elif cla=="40":result+='d'
    elif cla=="20":result+='c'
    elif cla=="10":result+='p'
    else:
        print("该系统无此文件类型")
        sys.exit()
    for site in chomd:
        if site=="7":result+='rwx'
        elif site=="6":result+='rw-'
        elif site=="5":result+='r-x'
        elif site=="4":result+='r-x'
        elif site=="3":result+='-wx'
        elif site=="2":result+='-w-'
        elif site=="1":result+='--x'
        elif site=="0":result+='---'
        else:print("hahaha")
    return result
'''
    文件的最后修改时间离现在不到6个月的
    就会只显示月/日/小时:分钟，否在就会显示月/日/年.
    所以需要判断,我们用一个deal_time函数来处理
 '''
def deal_time(last_modtime):
    time = datetime.datetime.fromtimestamp(last_modtime)
    #判断时间是否超过六个月
    if (time+relativedelta(months=6))>datetime.datetime.now():
        time = time.strftime("%m月 %d %H:%M")
    else:
        time = time.strftime("%m月 %d  %Y")
    return time
#计算总用量
def deal_total(show_list,dir_now,dir_index=-1):
    total = 0
    dir_index += 1
    while  dir_index < len(show_list) and show_list[dir_index][0]!="-":
        total+=os.path.getsize(dir_now+'/'+show_list[dir_index])
        dir_index+=1
    total = (round(total/4096)+1)*4
    print('总用量 ' + str(total))
#ls命令
def cmd_ls(attribute,dir_name):
    file_list = []
    show_list = []
    dir_now = '.'
    if not dir_name:
        file_list.extend(os.listdir(os.path.abspath(os.curdir)))
    else:
        for dir in dir_name:
            if not os.path.isdir(dir):
                if os.path.isfile(dir):
                    file_list.append(dir)
            else:
                file_list.append('-'+dir)
                file_list.extend(os.listdir(dir))
    #a属性
    if 'a' not in attribute:
        for file in file_list:
            if file[0]!='.':
                show_list.append(file)
    else:
        show_list = file_list
        flag_num = 0
        #print(show_list)
        #需要在每一个文件夹属性下加入.和..
        for index in range(len(show_list)):
            if show_list[index][0]=="-":
                show_list[index+1:index+1]=['.','..']
                flag_num+=1
        if flag_num == 0:
            show_list[0:0]=['.','..']
    #l属性
    if 'l' in attribute:
        if show_list[0][0]!='-':
            deal_total(show_list,os.path.abspath(os.curdir))
        for file in show_list:
            if file.startswith('-'):
                dir_now = file[1:]
                print('/'+file[1:]+":")
                deal_total(show_list,dir_now,show_list.index(file))
            else:
                path_now =dir_now+"/"+file
                file_stat = os.stat(path_now)
                #硬连接数
                link_num =file_stat.st_nlink
                uid_name = pwd.getpwuid(file_stat.st_uid).pw_name
                gid_name = pwd.getpwuid(file_stat.st_gid).pw_name
                file_size = file_stat.st_size
                last_modify_time =deal_time(file_stat.st_mtime)
                class_chomd=class_chomd_fmt(oct(file_stat.st_mode)[2:])
                print('{0:<10} {1:^5} {2:<10} {3:<10} {4:>5} {5:^10} {6:<}'.format(class_chomd,link_num,uid_name,gid_name,file_size,last_modify_time,file))
    else:
        for file in show_list:
            if file.startswith('-'):
                if show_list.index(file)!=0:
                    print('')
                print('/' + file[1:] + ":")
            else:
                print(file,end=" ")
        print("")

def cmd_touch(attribute,dir_name):
    pass
def main():
    cmd_list = ('ls', 'touch')
    dir_name = []
    attribute = []
    cmd_name = ''
    if len(sys.argv) >= 2:
        cmd_name = sys.argv[1]
        for argv in sys.argv[2:]:
            if argv.startswith('-'):
                attribute.append(argv)
            else:
                dir_name.append(argv)
        dir_name = list(set(dir_name))
        attribute = list(set(attribute))
        #将-la此类分离开来 如-la -k -dh分为['l','a','k','d','h']
        for attr in range(len(attribute)):
            if len(attribute[attr]) > 2:
                for i in range(len(attribute[attr]) - 1):
                    attribute.append(attribute[attr][i + 1])
                attribute.remove(attribute[attr])
            else:
                attribute[attr] = attribute[attr][1]
    else:
        print("错误!没有命令")
    # print(attribute)
    if cmd_name in cmd_list:
        if cmd_name == 'ls':
            cmd_ls(attribute, dir_name)
        elif cmd_name == 'touch':
            cmd_touch(attribute, dir_name)
    else:
        print("系统没有该名令")
        sys.exit()

if __name__ == '__main__':
    main()










