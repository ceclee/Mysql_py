
import pymysql
# 打开数据库连接
db = pymysql.connect('localhost','root','123456',charset = 'utf8')
# 创建游标对象
cur = db.cursor()
# 创建ku
try:
    cur.execute('create database python;')
    cur.execute('use python;')
    cur.execute('create table t1(\
             id int primary key,\
             name varchar(20),\
             score tinyint unsigned);')
    cur.execute("insert into t1 values\
            (1,'吕布',88),\
            (2,'貂蝉',19),\
            (3,'无双',90);")
    db.commit()
    
except Exception as e:
    db.rollback()
    print('failed',e)

cur.close()
db.close()
              
