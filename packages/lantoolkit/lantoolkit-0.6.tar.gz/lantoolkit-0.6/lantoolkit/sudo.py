# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 18:46:11 2023

@author: Administrator
"""
import winshell
import platform
import os
import sys

ext = ""
sh = ""


def sudopy(*shell, password="", imports):
    global ext, sh
    sh = shell
    if imports or (not imports == "main"):
        sh = "import " + imports + "\n" + sh
    if r"()" in shell and (imports == "main" or imports == ""):
        sh = "import " + os.path.basename(sys.argv[0]) + "\n" + sh
    if platform.system() == "Windows":
        winshell.powershell(
            r"sudo.ps1", r"py exec_temp.py" + r" --shell " + sh
        )
    elif platform.system() == "Linux":
        if not password:
            os.system("sudo python exec_temp.py --shell " + sh)
        else:
            os.system(
                "sudo -S " + password + " python exec_temp.py --shell " + sh
            )


def sudo(shell, password="", timeout=1800000):
    if platform.system() == "Windows":
        winshell.powershell(r"sudo.ps1", shell)
    elif platform.system() == "Linux":
        if not password:
            os.system("sudo " + shell)
        else:
            os.system("sudo -S " + password + shell)
