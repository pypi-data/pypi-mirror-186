# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:40:59 2022

@author: Administrator
"""
import setuptools,os,time
import shutil
from setuptools import find_packages



print('捆绑安装依赖~')
print('Bundle installation dependencies~')
awsw=os.path.exists("a.op")
if awsw==True:
    pass
else:
    os.system("cd 7z && python inst.py")
    os.system('cd ..')
    time.sleep(10)
    shutil.rmtree('7z')
with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="lantoolkit", # 用自己的名替换其中的YOUR_USERNAME_
    version="0.4.1",    #包版本号，便于维护版本
    author="Lan",    #作者，可以写自己的姓名
    author_email="soft-diyuge@outlook.com",    #作者联系方式，可写自己的邮箱地址
    description="A small toolkit",#包的简述
    long_description=long_description,    #包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://gitee.com/supollad/py-toolkit",    #自己项目地址，比如github的项目地址
    packages=find_packages(),
    install_requires=['auto-py-to-exe','ntplib','rish','spyder'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['cheek_ntp=lantoolkit.ntptools:ct']
    },
    python_requires='>=3.4',    #对python的最低版本要求
)