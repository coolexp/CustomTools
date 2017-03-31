#coding=utf-8
import os
import sys
import codecs
import xlrd


def getTable(tableName, sheetName):
    data = xlrd.open_workbook(tableName)
    table = data.sheet_by_name(sheetName)
    nrows = table.nrows
    ncols = table.ncols
    f = codecs.open("ENUM\ErayTextEnum.h", "w", "utf-8")
    f.write(u"#ifndef _OFF__TEXT_TEXTVO_ID__H__\n")
    f.write(u"#define _OFF__TEXT_TEXTVO_ID__H__\n")
    f.write(u"enum TEXT_TEXTVO_ID{")
    f.write(u"\t\n")
    strTmp = u"\tTEXT_TEXTVO_ID_0=0,"
    f.write(strTmp)
    for r in range(5,nrows):
        f.write(u"\t\n")
        for c in range(ncols - 2):
            strCellValue = u""
            CellObj = table.cell_value(r, c)
            value = str(int(CellObj))
            if r==5:
                strTmp = u"\tTEXT_TEXTVO_ID_"+ value+"=1,"
            else:
                 strTmp = u"\tTEXT_TEXTVO_ID_"+ value+","
            f.write(strTmp)
    f.write(u"\n};")
    f.write(u"\n#endif")
    f.close()
def main():
    #getTable(u"C:\\Projects\\OFF\\07_SRC\\DATA\\Text.xls", u"Text")
    showSheets()

def showSheets():
    xls = u"..\\xls\\Language.xlsx"
    book = xlrd.open_workbook(xls)
    for sheet in book.sheets():
        print(sheet.name)
        nrows = sheet.nrows
        ncols = sheet.ncols
        for c in range(1,ncols):
            print sheet.cell_value(0, c)
            for r in range(1,nrows):
                print("%s->%s"%(sheet.cell_value(r,0),sheet.cell_value(r, c)))
        print(nrows,ncols)

def generateBroadCastType():
    tableName = u"C:\\Projects\\OFF\\07_SRC\\DATA\\MailSystem.xls"
    sheetName = u"BrodcastTemp"
    data = xlrd.open_workbook(tableName)
    table = data.sheet_by_name(sheetName)
    nrows = table.nrows
    ncols = table.ncols
    f = codecs.open("ENUM\MailSystemBrodcastEnum.h", "w", "utf-8")
    f.write(u"#ifndef __OMGPro__MAILSYSTEM_BROADCASTVO_ID__H__\n")
    f.write(u"#define __OMGPro__MAILSYSTEM_BROADCASTVO_ID__H__\n")
    f.write(u"enum MAILSYSTEM_BROADCASTVO_ID{")
    for r in range(5,nrows):
        f.write(u"\t\n")
        for c in range(1,2):
            CellObj = table.cell_value(r, c)
            value = str(int(CellObj))
            strTmp = u"\tMAILSYSTEM_BROADCASTVO_"+ value+","
            f.write(strTmp)
    f.write(u"\n};")
    f.write(u"\n#endif")
    f.close()
if __name__ == "__main__":
    av = sys.argv
    if(os.path.exists("ENUM")==False):
        os.makedirs("ENUM")
    if(len(av)>1):
        type = str(av[1])
        if(type=="a"):
            main()
        elif(type=="b"):
            generateBroadCastType();
    else:
        main()
    print ("success")
