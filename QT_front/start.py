import msgWindow
import window
import post
from collections import defaultdict, OrderedDict

envirs=[]
database=[ ]


def initialization():
    data = {
        "version":"1.0",
    }
    resdata = post.requestPost(0 , data)
    envirs.extend(resdata["envirs"])
    database.extend(resdata["database"])
    print(envirs)
    print(database)

if __name__ == '__main__':

    try:
        initialization()
        result = window.main(envirs,database)
    except Exception as e :
        msgWindow.msg( "连接服务器失败" )
        print("退出")

    # commit(result)
