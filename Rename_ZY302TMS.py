# -*- encoding:utf-8 -*-
import os as OS



inPath = r'D:\宏观监测\快视图'

dirs = OS.listdir(inPath)

for f in dirs:

    # 原来快视图文件的路径
    oldfile = OS.path.join(inPath, f)
    
    filename = OS.path.splitext(f)[0]
    print (filename)

    #构造新快视图文件名和路径
    newname = OS.path.basename(filename) + '_quick' + '.PNG'
    newfile = OS.path.join(inPath, newname)

    
    OS.rename(oldfile, newfile)

print("succeed!!!")
