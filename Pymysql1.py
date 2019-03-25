
import pymysql
# 打开数据库连接
db = pymysql.connect('localhost','root','123456',charset = 'utf8')
# 创建游标对象
cur = db.cursor()
cur.execute('use python;')
cur.execute('select * from t1;')
One = cur.fetchone()
print(One)
print('*' * 30)
many = cur.fetchmany(2)
print(many)
# print('*' * 30)
# All = cur.fetchall()
# print(All)

cur.close()
db.close()
