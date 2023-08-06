# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:52:17 2023

@author: Administrator
"""
__all__ = [
    "archive",
    "file",
    "sudo",
    "pip",
    "ntp",
    "piptools",
    "winshell",
]
import platform
import os
import archive
import piptools, subprocess
import winshell

# logog=''''''
# logoe=''''''


def __runfst__():
    __fc = "Python Version:" + " " + platform.python_version()
    __et = "PKG Version:" + "0.3.2"
    print(__et)
    print(__fc)


# %%Gets the operating system type
if __name__ == "__main__":
    # %%Logo

    logo = """
    ╔════╦═══╦═══╦╗  ╔╗╔═╦══╦════╗
    ║╔╗╔╗║╔═╗║╔═╗║║  ║║║╔╩╣╠╣╔╗╔╗║
    ╚╝║║╚╣║ ║║║ ║║║  ║╚╝║ ║║╚╝║║╚╝
      ║║ ║║ ║║║ ║║║ ╔╣╔╗║ ║║  ║║
      ║║ ║╚═╝║╚═╝║╚═╝║║║╚╦╣╠╗ ║║
      ╚╝ ╚═══╩═══╩═══╩╝╚═╩══╝ ╚╝"""

    # %%Logo Operate

    # Do not run.
    # Debugging~
    # def __debuging__setlogo__(logof):
    #     global logoe
    #     logoe=logof
    # if logoe=='':
    #     pass
    # else:
    #     logo==logoe
    # def _nologo():
    #     global logog
    #     logog=''''''
    # if not logog=='':
    #     pass
    # if logog=='':
    #     logo==logog
    print(logo)
    __runfst__()


def python_call_powershell(file, *o):
    try:
        args = [
            r"powershell.exe",
            "-ExecutionPolicy",
            "Unrestricted",
            file,
            o,
        ]  # args参数里的ip是对应调用powershell里的动态参数args[0],类似python中的sys.argv[1]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        return dt
    except Exception as e:
        print(e)
    return False


class clear:
    def __init__(self):
        os.system("cls")


unarchive = archive.unfile
make_archive = archive.addfile
pip_install = piptools.install
pip_uninstall = piptools.uninstall
pip_reinstall = piptools.reinstall
pwh = winshell.powershell
