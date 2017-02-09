__author__ = 'sloppy'
import httplib,json

def checkTicket():
    jsonStr = json.dumps({"receipt-data": "sss"})
    connect = httplib.HTTPSConnection("sandbox.itunes.apple.com")
    headers = {"Content-type": "application/json"}
    connect.request("POST", "/verifyReceipt", jsonStr)
    result = connect.getresponse()
    respData = result.read()
    receipt = json.loads(respData)
    status = receipt[u'status']
    print(status)
if __name__ == "__main__":
    checkTicket()
