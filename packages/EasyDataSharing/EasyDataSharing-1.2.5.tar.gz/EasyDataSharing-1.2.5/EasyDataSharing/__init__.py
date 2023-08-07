import json
import math
import os,sys

basic  = {"data": [], "Alerts": 0, "Authors": []}
home = os.path.join(os.path.dirname(__file__))+ "/"
datas = {}
try:
    with open(home + "data.json") as f:
        datas = json.load(f)
except:
    with open(home + "data.json","a") as f:
        json.dump(basic,f)
    with open(home + "data2.json","a") as f:
        json.dump(basic,f)
    datas = basic

basicInfo = {"name": "","to": "","data": {}}
AlertsSize = 0

def IdFromAuthor(author):
    UpdateValue()
    return datas["Authors"].index(author)
    
def UpdateValue():
    global datas
    with open(home + "data.json") as f:
        while is_non_zero_file(home + "data.json") == False:
            pass
        datas = json.load(f)

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def getFrom(reader,author,id,ValueId):
    global datas
    UpdateValue()
    return datas["data"][id]["data"][ValueId]
def add(x, y):
    return x + y
def Alert():
    datas["Alerts"] = add(datas["Alerts"],1)
    UpdateValue()

def UpdateData(author,reader,ValueId,Value,id=-1):
    global datas
    if id == -1:
        datas["data"].append(basicInfo)
        id = len(datas["data"])-1
        datas["data"][id]["name"] = author
        datas["data"][id]["to"] = reader
        datas["data"][id]["data"][ValueId] = Value
        with open(home + "data.json","w+") as f:
            f.truncate(0)
            f.seek(0)
            datas["Authors"].append(author)
            Alert()
            json.dump(datas,f)
        return id
    if id == IdFromAuthor(author):
        datas["data"][id]["name"] = author
        datas["data"][id]["to"] = reader
        datas["data"][id]["data"][ValueId] = Value
        with open(home + "data.json","w+") as f:
            f.truncate(0)
            f.seek(0)
            Alert()
            json.dump(datas,f)
        return