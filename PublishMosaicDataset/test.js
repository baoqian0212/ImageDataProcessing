const {
    spawn
} = require('child_process');
const path=require('path')
// let _path = `D:\\innernetwork\\hainan\\cloud_app-1.2.0-win\\cloud_app.exe`;
// let arg = [
//     `isAutoUpload=true`,
//     `imagetype=3`,
//     'metaPath=E:\\Install\\云存储\\部署软件\\湖南\\湖南测试数据\\原始卫片\\GF1元数据.xls',
//     'dataPath=E:\\Install\\云存储\\部署软件\\湖南\\湖南测试数据\\原始卫片\\2019',
//     'quickPath=E:\\Install\\云存储\\部署软件\\湖南\\湖南测试数据\\原始卫片\\快视图',
//     'thumbPath=E:\\Install\\云存储\\部署软件\\湖南\\湖南测试数据\\原始卫片\\拇指图'
// ]
// let _path =path.resolve(process.cwd(),'tool/Debug/数据提取工具.exe');
// let metaPath=path.resolve(process.cwd(),'tool/meta.xlsx');
// let outPath=path.resolve(process.cwd(),'提取结果.xlsx');
// let inputPath=path.resolve(process.cwd(),'提取结果.xlsx');
let _path="C:\\Python27\\python.exe"
// let arg = [
//     `Excel`,//输出器类型
//     `元数据提取`,//提取器名称
//     'Xml',//解析格式(Excel;Mdb;Xml;Word;SMS)
//     'true',
//     '0',
//     '1',
//     '0',
//     '无',
//     metaPath,
//     inputPath,
//     outPath
// ]
// let arg = [
//     `Excel`,//输出器类型
//     `元数据提取`,//提取器名称
//     'Xml',//解析格式(Excel;Mdb;Xml;Word;SMS)
//     'true',
//     '0',
//     '1',
//     '0',
//     '无',
//     metaPath,
//     inputPath,
//     outPath
// ]
let arg = [
    `test.py`,
    `-n=test`,
    '-f=E:\\湖南项目\\04Python\\Test\\MosaicDataset\\MosaicDataset.gdb\\Fenfu'
    `-u=siteadmin`,
    '-p=siteadmin'
]
const bat = spawn(_path, arg);

bat.stdout.on('data', async (data) => {
    let stdout = data.toString();
    console.log('stdout==>', stdout);
});

bat.stderr.on('data', async (data) => {
    console.log('stderr==>', data.toString());
});

bat.on('exit', (code) => {
    console.log(`Child exited with code ${code}`);
});