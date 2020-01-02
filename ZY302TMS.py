# -*- coding: cp936 -*-
import os as OS
import sys as SYS
import shutil
import stat

"""
ZY302_TMS 中有部分有问题数据，本程序根据影像压缩文件大小区分，
将有问题数据：数据大小<1G ,放在test1文件夹中
正常数据：数据大小>1G,放在test2文件夹中
shutil.move（src, dst）方法实现
version :python37
"""

inPath = r'D:\ZY302-TMS'


dirs = OS.listdir(inPath)

for f in dirs:
    
    f_path = OS.path.join(inPath, f)

    # 查看文件大小，单位为bytes
    f_size = OS.path.getsize(f_path)
    f_size = f_size / 1024**3

    print(f_size)

    if f_size < 1:

        newfile = r'D:\test1'
        shutil.move(f_path, newfile)
        

    else:
        newfile = r'D:\test2'
        shutil.move(f_path,newfile)
    
    
print ("succeed!!!")
