import sys,os,stat,pwd
#ls命令
def cmd_ls(attribute,dir_name):
    file_list = []
    show_list = []
    dir_now = '.'
    if not dir_name:
        file_list.extend(os.listdir(sys.path[0]))
    else:
        for dir in dir_name:
            if not os.path.isdir(dir):
                if os.path.isfile(dir):
                    file_list.append(dir)
            else:
                file_list.append('-'+dir)
                file_list.extend(os.listdir(dir))
    if 'a' not in attribute:
        for file in file_list:
            if file[0]!='.':
                show_list.append(file)
    else:
        show_list = file_list
    if 'l' in attribute:
        for file in show_list:
            if file.startswith('-'):
                dir_now = file[1:]
                print(file[1:]+":")
            else:
                uid_name = pwd.getpwuid(os.stat(dir_now+"/"+file).st_uid).pw_name
                gid_name = pwd.getpwuid(os.stat(dir_now+"/"+file).st_gid).pw_name
                print('{0} {1} {2} {3}'.format(oct(os.stat(dir_now+"/"+file).st_mode)[-3:],uid_name,gid_name,file))
    else:
        for file in show_list:
            print(file,end=" ")
    return


def cmd_touch(attribute,dir_name):
    pass
#path = print(sys.path[0])
cmd_list =('ls','touch')
dir_name = []
attribute=[]
cmd_name = ''
if len(sys.argv)>=2:
    cmd_name = sys.argv[1]
    for argv in sys.argv[2:]:
        if argv.startswith('-'):
            attribute.append(argv)
        else:
            dir_name.append(argv)
    dir_name = list(set(dir_name))
    attribute = list(set(attribute))
##将-la此类分离开来
    for attr in range(len(attribute)):
        if len(attribute[attr])>2:
            for i in range(len(attribute[attr])-1):
                attribute.append(attribute[attr][i+1])
            attribute.remove(attribute[attr])
        else:
            attribute[attr] = attribute[attr][1]


else:
    print("错误!没有命令")
#print(attribute)
if cmd_name in cmd_list:
    if cmd_name == 'ls':
        cmd_ls(attribute,dir_name)
    elif cmd_name == 'touch':
        cmd_touch(attribute,dir_name)
else:
    print("系统没有该名令")
    sys.exit()










