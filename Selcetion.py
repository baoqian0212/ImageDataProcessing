# -*- coding: cp936 -*-

import os as OS
import sys as SYS
import shutil


inPath = r'D:\SV1\SV1第2批\2019\SV1'
inPath = inPath.encode('utf-8')


outPath = r'D:\Python\SV1'


def readTXT():
    f  = open('SV1.txt','r')
    i=0
    foldNames = []
    for line in f:
        
        foldName = line[:-5]
        
        foldNames.append(foldName)

            
    f.close()

    return foldNames

def copyFold(foldNames, inPath):

    for root, dirs, files in OS.walk(inPath):

        # 遍历所有的文件夹
        for d in dirs:
            
            if d in foldNames:
                print d
                satelliteFold = OS.path.join(root, d)
                dstSrcDir = OS.path.join(outPath, d)

                if OS.path.exists(dstSrcDir):
                    print dstSrcDir, '存在先删除'
                    shutil.rmtree(dstSrcDir)
                
                shutil.copytree(satelliteFold,dstSrcDir)

                print d + 'copy成功！'
    
    
if __name__ == '__main__':
     
    foldNames = readTXT()
    copyFold(foldNames, inPath)
