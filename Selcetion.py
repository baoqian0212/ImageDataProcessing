# -*- coding: cp936 -*-

import os as OS
import sys as SYS
import shutil


inPath = r'D:\SV1\SV1��2��\2019\SV1'
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

        # �������е��ļ���
        for d in dirs:
            
            if d in foldNames:
                print d
                satelliteFold = OS.path.join(root, d)
                dstSrcDir = OS.path.join(outPath, d)

                if OS.path.exists(dstSrcDir):
                    print dstSrcDir, '������ɾ��'
                    shutil.rmtree(dstSrcDir)
                
                shutil.copytree(satelliteFold,dstSrcDir)

                print d + 'copy�ɹ���'
    
    
if __name__ == '__main__':
     
    foldNames = readTXT()
    copyFold(foldNames, inPath)
