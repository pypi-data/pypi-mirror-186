# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:40:59 2022

@author: Administrator
"""
import setuptools, os
from setuptools import find_packages

import platform
import subprocess


def cmd(command, else_do=r'print("失败")'):
    subp = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    subp.wait()
    if subp.poll() == 0:
        print("CHEEK DONE.")
    else:
        exec(else_do)


print("捆绑安装依赖~")
print("Bundle installation dependencies~")
awsw = os.path.exists("a.op")
if awsw is True:
    pass
else:
    cmd(
        "7z",
        else_do="""
    if platform.system()=='Windows':
        if platform.machine()== 'AMD64' or '86' in platform.machine():
           os.system(r'copy win\x86\7z.exe lantoolkit\7z.exe /y')
        else:
            os.system(r'copy win\arm64\* lantoolkit\ /y')
    else:
        pwd=input("请告诉我你的sudo密码（你的数据不会被记录）:")
        os.system(r"cd linux")
        os.system(r"tar -jxvf p7z1602.tar.bz2")
        os.system(r"cd p7zip_16.02")
        os.system("echo "+pwd+r" | sudo  -S make ")
        os.system("echo "+pwd+r" | sudo  -S make install")
        os.system(r"cd ../")
        os.system(r"rmdir p7zip_16.02")
        os.system('echo "Done!"')""",
    )
with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lantoolkit",  # 用自己的名替换其中的YOUR_USERNAME_
    version="0.6",  # 包版本号，便于维护版本
    author="Lan",  # 作者，可以写自己的姓名
    author_email="soft-diyuge@outlook.com",  # 作者联系方式，可写自己的邮箱地址
    description="A small toolkit",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://gitee.com/supollad/py-toolkit",  # 自己项目地址，比如github的项目地址
    packages=find_packages(),
    install_requires=["auto-py-to-exe", "ntplib", "rich", "spyder"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["cheek_ntp=lantoolkit.ntptools:ct"]},
    python_requires=">=3.4",  # 对python的最低版本要求
)
