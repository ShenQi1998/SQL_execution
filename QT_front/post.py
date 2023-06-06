import requests
import json

url_init = "http://127.0.0.1:8000/initialization"
url_comm = "http://127.0.0.1:8000/commit"

# 输入json 返回 json

#处理提交的数据
def commit(envir , database , SQL):
    if(SQL == ""):
        print("执行SQL为空")
        return
    if( len(database) == 0 ):
        print("执行的数据库为空")
        return
    data = {
        "envir":envir,
        "database":database,
        "SQL":SQL
    }
    requestPost(1, data)

def requestPost(status , data):
    data = str(data)
    if status == 0:
        res = getEnvironment(data)
    elif  status == 1 :
        res = setSQL(data)
        
    return json.loads(res.text)
    

def getEnvironment(data):
    res = requests.post(url=url_init, data = data)
    return res

def setSQL(data):
    res = requests.post(url=url_comm, data = data)
    return res