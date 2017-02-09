#code=utf-8
__author__ = 'sloppy'
import web
import httplib,json,base64

urls = (
    '/', 'index',
    '/add(.*)','add'
)

class index:
    def checkTicket(self,data):
        #data = base64.encodestring(data)
        jsonStr = json.dumps({"receipt-data": data})
        return jsonStr
        connect = httplib.HTTPSConnection("sandbox.itunes.apple.com")
        headers = {"Content-type": "application/json"}
        connect.request("POST", "/verifyReceipt", jsonStr)
        result = connect.getresponse()
        respData = result.read()
        receipt = json.loads(respData)
        #status = receipt[u'status']
        return receipt
    def GET(self):
        args=web.input()
        name=args.get('name')
        return "Hello, world!"+name
    def POST(self):
        args=web.input()
        receiptData=args.get('receipt')
        res=self.checkTicket(receiptData)
        return res

class add:
    def GET(self):
        render = web.template.render('templates/')
        args=web.input()
        name=args.get('name')
        return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()