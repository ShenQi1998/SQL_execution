import os
import json


class MemoryCache:
    def __init__(self):
        self.config_data = {}
        self.envirList = []
        self.databaseList = []

    def initRead(self):
        #根路径
        current_directory = os.path.dirname(os.path.abspath(__file__))
        with open( current_directory + "/config.json" ,'r',encoding = 'utf-8') as fp:
            self.config_data = json.load(fp)
            print("正在配置参数完成>>>>>>>>>>>>>>>>>>>")

    def getData(self):
        return self.config_data

    def getEnvir(self):
        return list(self.envirList)

    def getDB(self):
        return list(self.databaseList)
    
    def chechConfigData(self):
        self.envirList =  self.config_data["database"].keys()
        for database in self.config_data["database"].values() :
            if( self.databaseList == []):
                self.databaseList = database.keys()
            else:
                if self.databaseList !=  database.keys():
                    raise Exception("错误，不同环境数据库不同")  


configData = MemoryCache()


