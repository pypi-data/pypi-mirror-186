import json,os

basic  = {"data": [], "Alerts": 0, "Authors": []}
home = os.path.join(os.path.dirname(__file__))+ "/"
datas = {}
try:
    with open(home + "data.json") as f:
        datas = json.load(f)
except:
    with open(home + "data.json","a") as f:
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

def getFrom(id,ValueId):
    global datas
    UpdateValue()
    return datas["data"][id]["data"][ValueId]
def add(x, y):
    return x + y

def UpdateData(author,reader,ValueId,Value,id=None):
    global datas
    if id == None:
        UpdateValue()
        datas["data"].append(basicInfo)
        id = len(datas["data"])-1
        if(author in datas["Authors"]):
            id = IdFromAuthor(author)
        datas["data"][id]["name"] = author
        datas["data"][id]["to"] = reader
        datas["data"][id]["data"][ValueId] = Value
        datas["Authors"].append(author)
        with open(home + "data.json","w") as f:
            f.seek(0)  # rewind
            json.dump(datas,f)
            f.truncate()
        return id
    if id >=0:
        UpdateValue()
        with open(home + "data.json","w") as f:
            f.seek(0)  # rewind
            f.truncate(0)
            datas["data"][id]["name"] = author
            datas["data"][id]["to"] = reader
            datas["data"][id]["data"][ValueId] = Value
            json.dump(datas,f)
        return