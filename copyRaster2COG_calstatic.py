# -*- encoding:utf-8 -*-
import arcpy as ARCPY
import os as OS
import sys as SYS
import time as TIME

reload(SYS)
SYS.setdefaultencoding('utf-8')
"""
将tif格式的影像数据转换为COG格式的影像数据
并计算统计值
version:python27
"""



##ARCPY.CheckOutExtension("Spatial")

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

    
    inFolder = r"D:\TempGXLData\GF1B"
    outFolder = r"D:\CopyRasters\GF1B_COG"
    workspace = []
    
    start = TIME.clock()
    workspace = clear_file(inFolder)
##    print workspace
    copy_raster(workspace, outFolder)

    end1 = TIME.clock()
    t1 = end1 -start

    ARCPY.AddMessage("Runtime is :" )
    m, s = divmod(t1, 60)
    h, m = divmod(m, 60)
    ARCPY.AddMessage("%02d:%02d:%02d" % (h, m, s))
    print "copy rasters succeed!"

    end2 = TIME.clock()   

    ARCPY.BuildPyramidsandStatistics_management(outFolder,
                                                "INCLUDE_SUBDIRECTORIES",
                                                "NONE",
                                                "CALCULATE_STATISTICS"
                                                )
    
    t2 = end2 - end1

    ARCPY.AddMessage("Runtime is :" )
    m, s = divmod(t2, 60)
    h, m = divmod(m, 60)
    ARCPY.AddMessage("%02d:%02d:%02d" % (h, m, s))
    print "calculate statistics succeed!"

