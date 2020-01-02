# -*- coding: cp936 -*-
import arcpy as ARCPY
import os as OS
import sys as SYS

"""
将tif格式的影像数据转换为COG格式的影像数据
version:python27
"""

def clear_file(Directory):

    # 获取目录下的文件和文件夹
    dirs = OS.listdir(Directory)
##    print dirs

    #遍历目录下的文件
    for d in dirs:
        
        # 拼接到当前目录
        f=OS.path.join(Directory,d)
       
        #判断是否是文件
        if OS.path.isfile(f):

            workspace.append(Directory)

        else:
            clear_file(f)

    return workspace


def copy_raster(workspace, outFolder):

    for ws in workspace:
        try:
            ARCPY.env.workspace = ws
            rasters = ARCPY.ListRasters("*", "tif")
            print rasters
            for ras in rasters:
                print(ras)
                out_raster = OS.path.join(outFolder, ras)
                ARCPY.CopyRaster_management(ras, out_raster,
                                            nodata_value ="256",
                                            pixel_type = "8_BIT_UNSIGNED",
                                            format="Cloud Optimized GeoTIFF")
                print(ras + " " + "copy succeed")

        except:
            e = SYS.exc_info()[1]
            ARCPY.AddError(e.args[0])


if __name__ == '__main__':

    inFolder = r"D:\TempGXLData\SV1\2019"
    outFolder = r"D:\CopyRasters\SV1_COG"
    workspace = []

    workspace = clear_file(inFolder)
    print workspace
    copy_raster(workspace, outFolder)

