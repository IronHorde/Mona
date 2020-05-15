#-*- coding: utf-8 -*-
#模拟linux ls
import click
import sys
import os
import datetime
import pwd
from dateutil.relativedelta import relativedelta

file_list = []

def ls_init():
    '''
    初始化中需要ls中需要加在文件
    :return: None
    '''
    global  file_list
    file_list.extend(os.listdir(os.path.abspath(os.curdir)))
    file_list.sort()
    for file in file_list:
        if file[0] != '.':
           file_list.remove(file)

def display(show_list):
    '''
     将ls命令中的文件名普通
    :param show_list: 此参数为将要打印出的文件名列表
    :return: None
    '''
    for file in show_list:
        print(file,end=" ")
    print(' ')


def deal_total(show_list):
    '''
    计算当前目录的总用量
    :param show_list: 此参数为将要打印出的文件名列表
    :return:返回一个整数 如:80
    '''
    total = 0
    for dir_index in range(len(show_list)):
        if os.path.isdir(show_list[dir_index]):
            total += 1
        else:
            total += int(os.path.getsize(show_list[dir_index]) / 4096) + 1
        dir_index += 1
    total = total * 4
    return total


def class_chmod_fmt(class_chmod):
    '''
    将python获取的文件类型权限由八进制数转化为字符串形式
    :param class_chmod:文件类型与文件权限 如：’40777‘
    :return:转化之后的字符串 如：‘drw-rw-rw-’
    '''
    clazz = {'140': 's','120': 'l','100': '-','60': 'b','40': 'd','20': 'c','10': 'p'}
    chmods = {'7': 'rwx','6': 'rw-','5': 'r-x','4': 'r--','3': '-wx','2': '-w-','1': '--x','0': '---'}
    cla = class_chmod[:-3]
    chmod = class_chmod[-3:]
    result = ''
    result+=clazz[cla]
    for site in chmod:
       result+=chmods[site]
    return result


def deal_time(last_modtime):
    '''
    将时间戳转换为如下格式
    文件的最后修改时间离现在不到6个月的
    就会只显示月/日/小时:分钟，否在就会显示月/日/年.
    :param last_modtime:
    :return:None
    '''
    print(last_modtime)
    time = datetime.datetime.fromtimestamp(last_modtime)
    if (time + relativedelta(months=6)) > datetime.datetime.now():
        time = time.strftime("%-m月 %-d %H:%M")
    else:
        time = time.strftime("%-m月 %-d  %Y")
    return time


def ls_option_a():
    '''
    ls中的a属性
    :return:None
    '''
    global file_list
    file_list=[]
    file_list.extend(os.listdir(os.path.abspath(os.curdir)))
    file_list[0:0] = ['.','..']



def ls_option_l():
    '''
    ls中的l属性
    :return:None
    '''
    global file_list
    total=deal_total(file_list)
    print('总用量：'+str(total))
    for file in file_list:
            path_now = file
            file_stat = os.stat(path_now)
            # 硬连接数
            link_num = file_stat.st_nlink
            uid_name = pwd.getpwuid(file_stat.st_uid).pw_name
            gid_name = pwd.getpwuid(file_stat.st_gid).pw_name
            file_size = file_stat.st_size
            last_modify_time = deal_time(file_stat.st_mtime)
            class_chomd = class_chmod_fmt(oct(file_stat.st_mode)[2:])
            print('{0:<10} {1:^5} {2:<10} {3:<10} {4:>5} {5:^10} {6:<20}'.format(class_chomd,link_num,uid_name,
                                                                                 gid_name,file_size,
                                                                                 last_modify_time,file))


@click.command()
@click.option('-a','--all',default = False,help='显示全部文件')
@click.option('-l','--long',default = False,help='查看详细信息')
def cmd_ls(**options):
    '''
    利用不同属性进行不同操作
    :param options:所有属性的集合
    :return:
    '''
    global file_list
    ls_init()
    if options['all'] and not options['long']:
        ls_option_a()
        display(file_list)
    if options['long'] and not options['all']:
        ls_option_l()
    if options['long'] and options['all']:
        ls_option_a()
        ls_option_l()
    if not options['long'] and not options['all']:
        display(file_list)

if __name__ == '__main__':
    cmd_ls()



