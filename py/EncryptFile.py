#coding=utf-8
__author__ = 'sloppy'
from base64 import b64encode
from base64 import b64decode

def encodeImage(inputFile,outputFile):
    print("start encode")
    with open(inputFile,'rb') as InputFile:
        data = InputFile.read()
        mage_64_encode = b64encode(data)
        outputFile = open(outputFile,"wb")
        outputFile.write(mage_64_encode)
        outputFile.close()
        InputFile.close()
    print("end encode")
def decodeImg(inputFile,outputFile):
    print("start decode")
    with open(inputFile,'rb') as InputFile:
        data = InputFile.read()
        data_file_decode =b64decode(data)
        d = open(outputFile,"wb")
        d.write(data_file_decode)
        d.close()
        InputFile.close()
    print("end decode")
if __name__=="__main__":
    encodeImage(r"G:\E:\Media\images\1.jpg",r"G:\E:\Media\images\1_e.jpg");
    decodeImg(r"G:\E:\Media\images\1_e.jpg",r"G:\E:\Media\images\1_d.jpg")