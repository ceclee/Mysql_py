
import pymysql
# 打开数据库连接
db = pymysql.connect('localhost','root','123456',charset = 'utf8')
cur = db.cursor()
cur.execute('use python')
id1 = input('input id:')
name = input('请输入姓名:')
score = input('请输入chengji:')
ins = 'insert into t1(id,name,score) values (%s,%s,%s)'
cur.execute(ins,[id1,name,score])  
#execute 第二个占位一定要是列表！！！！
#第二种```values('%s','%s') %(name,score)
db.commit()
cur.close()
db.close()
