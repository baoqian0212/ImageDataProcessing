# -*- coding:utf-8 -*-
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
import arcpy as ARCPY
import shutil as SHUTIL
import os as OS
import argparse as ARCPARSE
import time as TIME

generalfolder = OS.getcwd()

def inputargs():
    parser = ARCPARSE.ArgumentParser(description='manual to this script')
    parser.add_argument('-n', '--ServiceName', type=str,
                        default=None, help='eg: Service Name, suchas MyImageService')
    parser.add_argument('-f', '--MosaicDataset', type=str,
                        default=None, help='eg: MosaicDataset will be publish as Service')
    parser.add_argument('-u', '--UserName', type=str,
                        default=None, help='eg: ArcGIS Server UserName')
    parser.add_argument('-p', '--Password', type=str,
                        default=None, help='eg: ArcGIS Server Password')
    args = parser.parse_args()

    ServiceNametag = args.ServiceName
    mdpath = args.MosaicDataset
    username = args.UserName
    password = args.Password

    print "===========this is argument============="
    print "ServiceName : ", ServiceNametag
    print "MosaicDataset : ", mdpath
    print "ArcGIS Server UserName : ", username
    print "ArcGIS Server Password : ", password

    return ServiceNametag, mdpath, username, password

def publish(servicename, mdpath, username, password):
    # Step1 创建GIS服务器连接文件
    print u'Step1 创建GIS服务器连接文件'

    connecttype = 'ADMINISTER_GIS_SERVICES'

    outdir = OS.path.join(generalfolder, 'PublishImageService')
    if OS.path.exists(outdir):
        SHUTIL.rmtree(outdir)
    OS.mkdir(outdir)

    out_folder_path = outdir
    out_name = 'ConnectToArcGISServer.ags'
    server_url = 'https://localhost:6443/arcgis/admin'
    use_staging_folder = False
    staging_folder_path = outdir
    username = username
    password = password

    ARCPY.mapping.CreateGISServerConnectionFile(connecttype,
                                                out_folder_path,
                                                out_name,
                                                server_url,
                                                "ARCGIS_SERVER",
                                                use_staging_folder,
                                                staging_folder_path,
                                                username,
                                                password,
                                                "SAVE_USERNAME")

    print '      ' + out_name.decode('utf-8') + u' 已创建'


    # Step2 创建影像服务定义草稿文件(.sddraft)

    print u'Step2 创建影像服务定义草稿文件...'

    connoctionfile = OS.path.join(outdir, out_name)
    service = servicename
    sddraft = OS.path.join(outdir, service + '.sddraft')

    ARCPY.CreateImageSDDraft(mdpath, sddraft, service,
                            'ARCGIS_SERVER', copy_data_to_server=False)
    print '      ' + service + '.sddraft' + u'  已创建'

    # Step3 分析服务定义草稿
    print u'Step3 分析服务定义草稿文件...'
    analysis = ARCPY.mapping.AnalyzeForSD(sddraft)

    print(u"     分析服务定义草稿结果: ")
    for key in list(analysis.keys()):
        print("      ---{}---".format(key.upper()))
        for ((message, code), layerlist) in analysis[key].items():
            print("        (CODE {})  {} ".format(code, message))

    # Step4  过渡 sddraft 到服务定义文件sd
    print u'Step4  过渡 sddraft 到服务定义文件sd...'
    outSDfile = OS.path.join(outdir, service+".sd")

    ARCPY.StageService_server(sddraft, outSDfile)
    print u'      Done!'

    # Step5 将服务定义文件发布到服务器
    print u'Step5 将服务定义文件发布到服务器...'
    inSdFile = outSDfile
    inServer = connoctionfile
    inServiceName = service

    ARCPY.UploadServiceDefinition_server(inSdFile, inServer, inServiceName)
    print u'      Done!'


if __name__ == '__main__':
    try:
        ServiceNametag, mdpath, username, password = inputargs()
        publish(ServiceNametag, mdpath, username, password)
    except Exception, e:
        print "%Fail%", str(e)
