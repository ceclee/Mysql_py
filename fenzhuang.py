
import pymysql

class Mysqlpy:
    def __init__(self,database,host='localhost',user='root',password='123456',
                                                            charset='utf8',
                                                            port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port
        

    def open(self):
        self.db = pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   charset=self.charset,
                                   port=self.port)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def zhixing(self,sql,L=[]):
        self.open()
        self.cursor.execute(sql,L)
        self.db.commit()
        self.close()


    def all(self,sql,L=[]):
        self.open()
        self.cursor.execute(sql,L)
        result = self.cursor.fetchall()
        self.close()
        return result

if __name__ == "__main__":
    sqlh = Mysqlpy('python')
    sqlh.zhixing('use python')
    sqlh.zhixing('insert into t1(id,name,score) values (%s,%s,%s)',[45,'ui',43])
