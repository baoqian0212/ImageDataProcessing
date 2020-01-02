# -*- coding: cp936 -*-
import arcpy as ARCPY
import os as OS
import sys as SYS

"""
��tif��ʽ��Ӱ������ת��ΪCOG��ʽ��Ӱ������
version:python27
"""

def clear_file(Directory):

    # ��ȡĿ¼�µ��ļ����ļ���
    dirs = OS.listdir(Directory)
##    print dirs

    #����Ŀ¼�µ��ļ�
    for d in dirs:
        
        # ƴ�ӵ���ǰĿ¼
        f=OS.path.join(Directory,d)
       
        #�ж��Ƿ����ļ�
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

