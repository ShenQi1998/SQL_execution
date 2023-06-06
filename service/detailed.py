import pymysql
import json
from collections import defaultdict, OrderedDict

def handle(tranCode , Dict):
    print(tranCode)
    if(tranCode=='initialization'):
        respondDictDict = initialization()
    elif(tranCode=='commit'):
        respondDictDict = commit(Dict)
    result = json.dumps(respondDictDict, sort_keys=True, indent=4, separators=(',', ':'))
    return result

def initialization():
    respondDict = defaultdict(list)
    respondDict["envirs"].extend(["DEV","SIT1","SIT2","UAT1"])
    respondDict["database"].extend(['db-1' , 'db-2' , 'db-3' , 'db-4' , 'db-5' , 'db-6' , 'db-7' ])
    respondDict["version"].extend([ "1.0" , "1.1" , "1.2"])
    return respondDict
    

def commit(Dict):
    print(Dict["SQL"])
    print(Dict["database"])
    print(Dict["envir"])
    respondDict = defaultdict(list)
    respondDict["status"] = "S"
    return respondDict
