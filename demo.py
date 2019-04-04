# -*- coding:utf-8 -*-
import MySQLdb
import config as cfg
from prettytable import PrettyTable

# 建立连接
try:
    try:
        db = MySQLdb.connect(
            host=cfg.HOST,  # mysql url
            user=cfg.USER,  # mysql username
            password=cfg.PASSWORD,  # mysql username's password
            db=cfg.DATABASE,    # operate database
            charset=cfg.CHARACTER)  # default character
        print('********************connection successfully********************')
    except Exception as e:
        print('********************connection fail********************')
        print('connection fail,the reason is {}'.format(e))
    cur = db.cursor()  # 建立游标（有了游标才能操作数据库）
    try:
        select_sql = 'SELECT * FROM nb_alarm_status;'  # sql语句 <查询语句>
        cur.execute(select_sql)  # 执行sql查询语句
        res = cur.fetchall()  # 获取所有查询结果;fetchone(),获取一条查询记录
        # PrettyTable美化输出结果
        db_result = PrettyTable(
            ['id', 'imei', 'device_id', 'stu_code', 'status', 'creator', 'create_date', 'updator', 'update_date'])
        for row in res:
            id = row[0]
            imei = row[1]
            stu_code = row[2]
            device_id = row[3]
            status = row[4]
            creator = row[5]
            create_date = row[6]
            updator = row[7]
            update_date = row[8]
            db_result.add_row([id, imei, stu_code, device_id, status, creator, create_date, updator, update_date])
        print(db_result)
        print('********************select successful********************')
    except Exception as e:
        print('查询失败 -- {}'.format(e))

    try:
        insert_sql = "INSERT INTO nb_alarm_status(id,imei,device_id,stu_code,status,creator,create_date,updator," \
                     "update_date) VALUES(0, '869662034322599', " \
                     "'4664fdd9-c258-42a1-a3ee-5er6ba1967cb', '8696620343292572ccfb7c5-094b-ab', '2', NULL, " \
                     "NOW(), NULL, NOW());"         # primary key is id
        delete_sql = "DELETE FROM nb_alarm_status WHERE id='1104982367744954677';"  # delete sql
        update_sql = "UPDATE nb_alarm_status SET creator=1 WHERE id='1104982367744954678';"
        update_sql_1 = "UPDATE nb_alarm_status SET tt=UNIX_TIMESTAMP(tt);"          # update sql --> datetime to stamp
        update_sql_2 = "UPDATE nb_alarm_status SET tt=FROM_UNIXTIME(tt);"           # update sql --> stamp to datetime
        alter_sql = "ALTER TABLE nb_alarm_status ADD Tname VARCHAR(20) DEFAULT NULL;"    # add column
        alter_sql_1 = "ALTER TABLE nb_alarm_status DROP Tname;"                       # delete column
        alter_sql_2 = "ALTER TABLE nb_alarm_status CHANGE chtime tt VARCHAR(20);"     # change column name
        alter_sql_3 = "ALTER TABLE nb_alarm_status MODIFY tt VARCHAR(20);"            # modify column type

        cur.execute(insert_sql)     # execute --执行sql语句
        db.commit()                 # commit  --提交操作，否则不会执行成功
        print('********************execute successful********************')
    except Exception as e:
        print('execute fail -- {}'.format(e))
except Exception as e:
    print('operation fail {}'.format(e))
