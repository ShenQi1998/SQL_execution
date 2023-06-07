import pymysql

def execute(Dict , config_data):
    database = config_data["database"][Dict["envir"]]
    print(Dict["envir"])
    print(Dict["database"] )
    print(Dict["SQL"] )

    SQL = Dict["SQL"].replace("\n" , "").rstrip() 
    sqls = SQL.split(";")

    for db_name in Dict["database"] :
        config_db = database[db_name]
        print(config_db)
        db_connect =pymysql.connect(
            host =  config_db["host"] ,
            port = config_db["port"],
            user = config_db["user"],
            password = config_db["password"],
            db = db_name
        )
        cursor = db_connect.cursor()

        for sql in sqls :
            if(sql != ""):
                cursor.execute(sql)

        #TODO 解决事务问题
        db_connect.commit()
        db_connect.close()
