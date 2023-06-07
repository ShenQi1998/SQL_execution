from  config import configData


def execute( envir ,database , SQL  ):
    data = configData.getData()
    print( data["DATABASE"]["DEV"]["db_1"] )


