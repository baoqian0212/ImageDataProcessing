# -*- encoding:utf-8 -*-
import os as OS

"""
复制快视图后需修改文件名，将*.jpg 修改为*_quik.PNG

版本 ：python 3.7
"""



inPath = r'D:\问题数据\快视图'

dirs = OS.listdir(inPath)

for f in dirs:

    oldfile = OS.path.join(inPath, f)
    newname = OS.path.basename(f) + '_quick' + '.PNG'
    newfile = OS.path.join(inPath, newname)
    OS.rename(oldfile, newfile)

print("succeed!!!")
