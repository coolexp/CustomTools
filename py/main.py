#coding=utf-8
import  xml.dom.minidom
import sys,os
from socket import *
from time import ctime
def testXML():
    dom = xml.dom.minidom.parse('abc.xml')
    root = dom.documentElement
    print root.nodeName
    print root.nodeValue
    print root.nodeType
    assert isinstance(root.ELEMENT_NODE, object)
    print root.ELEMENT_NODE

def printAllFiles(path):
    for root,dirs,files in os.walk(path):
        for one in files:
            print one
def test():
    t = 12345,23456,"HelloWorld"
    print t[0]
    print t

def updateHandler():
    print "updateHandler"

def initSock():
    sock = socket(AF_INET,SOCK_STREAM)
    ADDR=("10.10.10.111", 8088)
    sock.bind(ADDR)
    sock.listen(5)
    while True:
        print "waiting for connectiong"
        tcpClient,addr = sock.accept()
        print ('connect from',addr)
        s  = 'Hello world %s' %(ctime())
        tcpClient.send(s.encode("utf-8"))
        while True:
            try:
                data = tcpClient.recv(1024)
            except:
                print("exception")
                tcpClient.close()
                break
            if not data:
                print("invalid data")
                break;
            else:
                print data

    tcpClient.close()
    sock.close()

if __name__ == '__main__':
    print sys.argv[0]
    initSock()
    printAllFiles(".")