#coding=utf-8
__author__ = 'sloppy'
import httplib
import urllib

def testClient():
    c = httplib.HTTPConnection("www.baidu.com")
    c.request("GET", "/")
    response = c.getresponse()
    print response.status, response.reason
    data = response.read()
    print data

def sendhttp():
    data = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = httplib.HTTPConnection('bugs.python.org')
    conn.request('POST', '/', data, headers)
    httpres = conn.getresponse()
    print httpres.status
    print httpres.reason
    print httpres.read()

if __name__ == "__main__":
    testClient()