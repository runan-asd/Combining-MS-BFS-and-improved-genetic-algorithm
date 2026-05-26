import json
import os
class Databases:
    def __init__(self):
        self.users = json.loads(open(os.getcwd() + r"\GUI\users.json", mode='r', encoding='utf-8').read())
    
    def check_login(self,username,password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, '登陆成功'
                else:
                    return False, '登录失败，密码错误'
        return False, '登录失败，用户名不存在'
        

db = Databases()
if __name__ == '__main__':
    print(db.check_login('admin','123456'))
