# -*- coding: cp936 -*-
import os as OS
import sys as SYS
import shutil
import stat

"""
ZY302_TMS ���в������������ݣ����������Ӱ��ѹ���ļ���С���֣�
�����������ݣ����ݴ�С<1G ,����test1�ļ�����
�������ݣ����ݴ�С>1G,����test2�ļ�����
shutil.move��src, dst������ʵ��
version :python37
"""

inPath = r'D:\ZY302-TMS'


dirs = OS.listdir(inPath)

for f in dirs:
    
    f_path = OS.path.join(inPath, f)

    # �鿴�ļ���С����λΪbytes
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
