
from fenzhuang import Mysqlpy
from hashlib import sha1
sqlh = Mysqlpy('python')

menu = '''(1)注册
(2)登录
(q)退出
请选择(1/2/q)：'''

while True:
    choice = input(menu)
    if choice.strip() in '12q':
        if choice.strip() == '1':
            uname = input("输入姓名:") 
            sel = 'select username from user where username=%s'
        
            result = sqlh.all(sel,[uname])
            if len(result) != '':
                print('existed')
                break
            else:
                pwd1 = input('code:')
                pwd2 = input('code:')
                if pwd1 == pwd2:
                    #创建sha1加密对象;进行加密；返回十六进制的加密结果
                    s = sha1()
                    #不能是str,必须为字节流bytes!解码解出来的是str,转码出来的是bytes
                    s.update(pwd1.encode('utf-8'))
                    pwd = s.hexdigest() 
                    print(pwd)
                    #存数据库
                    ins = 'insert into user values(%s,%s)'
                    sqlh.zhixing(ins,[uname,pwd])
                    print('success!')
                else:
                    print('error code')



        elif choice.strip() == '2':
            uname = input('name:')
            pwd = input('code:')
            sel = 'select password from user where username=%s'
            result = sqlh.all(sel,[uname])
            s = sha1()
            s.update(pwd.encode('utf-8'))
            pwd = s.hexdigest()
            if len(result) == 0:
                print('no user')
            elif result[0][0] == pwd:
                print('success')
            else:
                print('code error')
        else:
            print('无效的选择')