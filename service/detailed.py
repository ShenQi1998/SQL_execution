import json
from collections import defaultdict, OrderedDict
import execute

def handle(tranCode , Dict ,  config_data , config_env , config_db ):
    print(tranCode)
    print(config_data)
    print(config_env)
    if(tranCode=='initialization'):
        respondDictDict = initialization(Dict , config_env , config_db )
    elif(tranCode=='commit'):
        respondDictDict = commit(Dict , config_data)
    result = json.dumps(respondDictDict, sort_keys=True, indent=4, separators=(',', ':'))
    return result

# 初始化
def initialization(Dict ,  config_env , config_db ):
    respondDict = defaultdict(list)
    if( not chechVersion(Dict["version"])):
        respondDict["status"] = "F"
        respondDict["msg"] = "当前版本过低"
    else:
        respondDict["status"] = "S"
        respondDict["envirs"].extend(config_env)
        respondDict["database"].extend(config_db)
    return respondDict


# 提交  
def commit(Dict , config_data):
    resultList = execute.execute(Dict , config_data )
    respondDict = defaultdict(list)
    respondDict["status"] = "S"
    return respondDict

#初始化时检查版本是否符合要求
def chechVersion(version):
    usedVersion = [ "1.0" , "1.1" , "1.2" ]
    if(version not in usedVersion):
        return False
    return True
