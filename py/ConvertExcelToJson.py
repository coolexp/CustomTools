#coding=utf-8
__author__ = 'sloppy'

import xlrd,codecs,os,json

def analysSheet(wb,sheetName,jsonList):
    sheet = wb.sheet_by_name(sheetName)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print("Rows:%i,Cols:%i"%(nrows,ncols))
    for r in range(5,nrows):
        jsonObj = {};
        jsonList.append(jsonObj)
        for c in range(0,ncols):
            CellObj = sheet.cell_value(r, c)
            jsonKey = u"%s"%sheet.cell_value(0,c)
            if jsonKey=="":
                continue
            jsonObj[jsonKey] = CellObj;
            #print ("Value:%s" % CellObj)
if __name__ == "__main__":
    print
    jsonPath=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,"res\data.json"))
    jsonFile = codecs.open(jsonPath,"w","gb2312")
    workbook = xlrd.open_workbook("C:\\Projects\\OFF\\07_SRC\\DATA\\MailSystem.xls")
    sheets = workbook.sheet_names()
    jsonObj = {}
    for sheet in sheets:
        #print sheet
        if sheet=='SheetsName':
            continue
        jsonObj[sheet] = []
        analysSheet(workbook,sheet,jsonObj[sheet])
    content = json.dumps(jsonObj)
    cc = content.decode("unicode_escape")
    jsonFile.write(cc)
    jsonFile.close()