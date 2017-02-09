#coding=utf-8
__author__ = 'sloppy'
import os
import sys
import codecs

def addFiles(path):
    print("start adding...")
    f = codecs.open("res/Animation.plist", "w", "utf-8")
    f.write(u'<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write(u'<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
    f.write(u'<plist version="1.0">\n')
    f.write(u'<dict>\n')
    f.write(u'\t<key>files</key>\n')
    f.write(u'\t<array>\n')
    for root, dirs, files in os.walk(path):
        for one in files:
            if one.find('.ExportJson')>0:
                f.write(u'\t\t<string>%s</string>\n'% one)
    f.write(u'\t</array>\n')
    f.write(u'</dict>\n')
    f.write(u'</plist>\n')
    f.close()
    print("add Complete")

if __name__ == "__main__":
    av = sys.argv
    addFiles("C:\\cocos-samples\\CocosGameCpp\\Resources\\animations")