#coding=utf-8
__author__ = 'sloppy'
from base64 import b64encode
from base64 import b64decode

def encodeImage():
    print("start encode")
    imgPath=r"C:\Projects\OFF\07_SRC\Client\res\ItemIcon\diamond2.png"
    with open(imgPath,'rb') as ImageFile:
        data = ImageFile.read()
        mage_64_encode = b64encode(data)
        image_64_decode =b64decode(mage_64_encode)
        print mage_64_encode
        img = open("1.png","wb")
        img.write(image_64_decode)
        img.close()
        ImageFile.close()
    print("end encode")

if __name__=="__main__":
    encodeImage()
