from config import configData
import multiSocket



if __name__ == "__main__":

    #读取配置文件
    configData.initRead()

    #校验配置文件信息
    configData.chechConfigData()
    data = configData.getData()

    # 启动socket
    multiSocket.startProcess()


