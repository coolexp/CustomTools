#coding=utf-8
__author__ = 'sloppy'
import sys,os
import ConfigParser
import subprocess

def pack():
    cfg = ConfigParser.ConfigParser()
    cfg.read("res/config.ini")
    tpCmd = cfg.get('cfg', 'TP')
    inPath = cfg.get('cfg', 'InPath')
    outPath = cfg.get('cfg', 'OutPath')
    list = os.listdir(inPath)
    for one in list:
        filePath = os.path.join(inPath,one)
        if os.path.isdir(filePath):
            subprocess.check_call("%s --data %s%s.plist --format cocos2d --sheet %s%s.png --size-constraints AnySize --force-squared --opt RGBA4444 --pack-mode Best %s%s" % (tpCmd,outPath,one,outPath,one,inPath,one))

    print "Success Pack"
    #print(inPath,outPath)
    #subprocess.Popen(['cocos', 'compile',])

if __name__ == '__main__':
    pack()