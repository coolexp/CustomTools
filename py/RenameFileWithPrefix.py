#coding=utf-8
__author__ = 'sloppy'
import sys,os

def changeFileName(path,prefix):
    for root, dirs, files in os.walk(path):
        for one in files:
            if one.find('.')>0:
                newName=prefix+one
                os.rename(os.path.join(root,one),os.path.join(root,newName))
    print("Rename Success!")

if __name__ == '__main__':
    argLen = len(sys.argv)
    if(argLen<2):
        print("Input Prefix Name")
    elif(argLen==2):
        changeFileName(".",sys.argv[1])
    else:
         changeFileName(sys.argv[1],sys.argv[2])