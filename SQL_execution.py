import cx_Oracle as cx  
import time

CO=[
    "ncbsco/GyIs#02n@188.177.163.240:1521/CBSDB", #开发
    "NCBSCO/NgWz#03h@188.177.167.240:1521/cbsdb", #SIT
    "NCBSCO/GyIs#02n@188.177.167.250:1521/cbsdb", #SIT3
    "ncbsco/NgWz#03h@188.177.177.240:1521/CBSDB", #SIT长周期
    "ncbsco/NgWz#03h@188.177.184.240:1521/sitzxdb",#SIT移植
    "NCBSCO/GyIs#02n@188.177.171.246:1521/cbsdb",   #UAT
    "NCBSCO/DlXi*01o@188.177.178.245:1521/uatldb",  #UAT长周期
    "NCBSCO/NgWz#03h@188.177.188.240:1521/uatzxdb", #UAT专项
    "NCBSCO/GyIs#02n@188.177.187.215:1521/orcl",  #性能测试
    "NCBSCO/NgWz#03h@188.177.177.240:1521/CBSDB"  #利息测试
    ]

CM =[
    "ncbscm/DlXi*02o@188.177.163.240:1521/CBSDB", #开发
    "NCBSCM/LyFn#03m@188.177.167.240:1521/cbsdb", #SIT
    "NCBSCM/DlXi*02o@188.177.167.250:1521/cbsdb",  #SIT3
    "ncbscm/LyFn#03m@188.177.177.240:1521/CBSDB", #SIT长周期
    "ncbscm/LyFn#03m@188.177.184.240:1521/sitzxdb",#SIT移植
    "NCBSCM/DlXi*02o@188.177.171.246:1521/cbsdb",   #UAT
    "NCBSCM/GyIs#01n@188.177.178.245:1521/uatldb"   #UAT长周期
    "NCBSCM/LyFn#03m@188.177.188.240:1521/uatzxdb", #UAT专项
    "NCBSCM/DlXi*02o@188.177.187.215:1521/orcl",  #性能测试
    "NCBSCM/LyFn#03m@188.177.177.240:1521/CBSDB"  #利息测试
]

GW=[
    "ncbsgw/AyAg*02h@188.177.156.125:1521/devel2",  #参数
    "ncbsgw/ZhYu#03b@188.177.177.240:1521/CBSDB",  #长周期
    "NCBSGW/AyAg*02h@188.177.166.250:1521/cbsdb" #SIT3
]

SQL =[
    "delete from kdpp_sundry where DEPT_PARM_NM in ('XHCRZYDM','XJXHZYDM')",
    "insert into kdpp_sundry (LGL_PERN_CODE, DEPT_PARM_NM, DEPT_PARM_DSC, DEPT_PARM_VAL, SERL_NUM_LONG, PARM_DATA, SPARE_DATA_750, BR_ID, MNTNC_TLR, MNTNC_ORG, MNTNC_DT, MNTNC_TM, TMSTP, REC_STE, AFFR_STE, GLBL_AFFR_RUNG_NUM, AFFR_STE_UPD_NUM, DATA_UPD_TMSTP, RECORD_CHANGE_TP, SPARE_FLD_01_32, SPARE_FLD_02_32) values ('9999', 'XHCRZYDM', '销户存入摘要代码', 'DP0243', 0, null, null, '01', '0', '0', '0', '0', 0, '0', 'O', '0', '0', null, null, null, null)",
    "insert into kdpp_sundry (LGL_PERN_CODE, DEPT_PARM_NM, DEPT_PARM_DSC, DEPT_PARM_VAL, SERL_NUM_LONG, PARM_DATA, SPARE_DATA_750, BR_ID, MNTNC_TLR, MNTNC_ORG, MNTNC_DT, MNTNC_TM, TMSTP, REC_STE, AFFR_STE, GLBL_AFFR_RUNG_NUM, AFFR_STE_UPD_NUM, DATA_UPD_TMSTP, RECORD_CHANGE_TP, SPARE_FLD_01_32, SPARE_FLD_02_32) values ('9999', 'XJXHZYDM', '现金转出', 'CM0010', 0, null, null, '01', '0', '0', '0', '0', 0, '0', 'O', '0', '0', null, null, null, null)"
]



if __name__=="__main__":
    cx.init_oracle_client(lib_dir=r"D:\software\PLSQL\instantclient_11_2")

    x=input("请输入CO/CM/GW\n")
    if x== 'CO':
        urls = CO
    elif(x== 'CM'):
        urls = CM
    elif(x == 'GW'):
        urls = GW
    else:
        raise Exception('请检查输入:' + x)

    for url in urls :
        try:
            con = cx.connect(url)
        except Exception as e:
            print("数据库连接失败")

        try: 
            for sql in SQL:
                cursor = con.cursor()       #创建游标
                cursor.execute(sql)         #执行sql语句
                cursor.close()              #关闭游标
            print(url + "       执行成功")
        except Exception as e:    
            # 回滚
            con.rollback()
            raise Exception("插入数据库错误！", e)

        con.commit()    #提交
        con.close()     #关闭数据库连接


'''
    更新日期
    20210612 V1.0 初版
'''

