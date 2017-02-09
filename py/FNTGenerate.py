#coding=utf-8
__author__ = 'sloppy'
import plistlib
import os
import re


def generate(fntName,plistSource,fntConfig):
    plistFile = '{0}.plist'.format(plistSource)
    info = plistlib.readPlist(plistFile)
    config = plistlib.readPlist(fntConfig)
    files = config.get("FNT_FILES")
    fileLen = len(files);
    f=open(fntName,'w')
    f.write('info face="Arial" size=32 bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=1,1 outline=0\n')
    f.write('common lineHeight={0} base=26 scaleW=128 scaleH=128 pages=1 packed=0 alphaChnl=0 redChnl=0 greenChnl=0 blueChnl=0\n'.format(config.get("Config")["lineheight"]))
    f.write('page id=0 file="{0}.png"\n'.format(plistSource))
    f.write('chars count={0}\n'.format(fileLen))
    _L = re.compile('{')
    _R = re.compile('}')
    for item in files:
        offsetInfo = info.get("frames")[item["img"]]["frame"]
        offsetInfo = _L.sub('',offsetInfo)
        offsetInfo = _R.sub('',offsetInfo)
        iList = offsetInfo.split(",")
        print offsetInfo
        f.write('char id={0}   x={1}    y={2}     width={3}    height={4}    xoffset=0     yoffset=0     xadvance={5}    page=0  chnl=15\n'.format(item["num"],iList[0],iList[1],iList[2],iList[3],iList[2]))
    #print('{0} is {1} years old. '.format(name, age)) #输出参数
    f.close()
if __name__ == '__main__':
    generate("fnt/NewJifen.fnt","PLIST/PublicSystem","FNT_CONFIG/FNT_1.plist")