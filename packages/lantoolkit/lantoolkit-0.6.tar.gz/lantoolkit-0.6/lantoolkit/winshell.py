# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 23:07:01 2023

@author: Administrator
"""
import subprocess


def powershell(file, o):
    try:
        # args参数里的ip是对应调用powershell里的动态参数args[0],类似python中的sys.argv[1]
        args = [r"powershell.exe", "-ExecutionPolicy",
                "Unrestricted", *file, *o]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        return dt
    except Exception as e:
        print(e)
    return False


def cmd(command,else_do=r'print("失败")'):
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, encoding="utf-8")
    subp.wait()
    if subp.poll() == 0:
        print('DONE.')
    else:
        exec(else_do)

# 如果报错，说禁止执行脚本，是因为没有权限，所以，把上面的一行代码换成
#args=[r"C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe","-ExecutionPolicy","Unrestricted", r"D:\jzhou\test_ping.ps1",ip]
