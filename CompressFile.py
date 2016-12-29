#coding=utf-8
__author__ = 'sloppy'

import zlib,os,struct,shutil,re

# 过滤不需要压缩的文件类型
SKIPS = (
    '.png',
    '.PNG',
    '.jpg',
    '.csb',
    '.ttf',
    '.mp3',
    '.fnt',
    '.py',
)
REC_SKIPS = re.compile('|'.join([re.escape(x) for x in SKIPS]), re.I)

# 创建不存在的文件夹
def createDir(outFile):
    path = "\\".join(outFile.split("\\")[:-1])
    if not os.path.exists(path):
        os.makedirs(path)

def compressOne(originalFile,outFile):
    infile = open(originalFile, 'rb')
    dst = open(outFile, 'wb')
    actualSize = os.path.getsize(originalFile)
    print("%s :actualSize:%i"% (originalFile,actualSize))
    compress = zlib.compressobj(9)
    # 添加文件压缩标记，并存储为网络字节序
    headBytes = struct.pack("!9sI","eraygames",actualSize)
    dst.write(headBytes)
    data = infile.read(1024)
    while data:
        dst.write(compress.compress(data))
        data = infile.read(1024)
    dst.write(compress.flush())

# path,需要压缩的文件夹，targetFolder压缩后的文件存放目标文件夹
def compressFile(path,targetFolder):
    for root, dirs, files in os.walk(path):
        for one in files:
            targetFile = '%s%s'% (targetFolder,os.path.join(root,one).replace(path,""));
            sourceFile = os.path.join(root,one);
            createDir(targetFile)
            if REC_SKIPS.search(one):
                shutil.copy(sourceFile,targetFile)
                continue
            compressOne(sourceFile,targetFile)
if __name__=="__main__":
    #创建目标文件夹
    path = 'C:\\Users\\sloppy\\Desktop\\res'
    workPath = '%s-c'% path;
    if not os.path.exists(workPath):
        os.makedirs(workPath)
    #开始压缩
    compressFile(path,workPath)
