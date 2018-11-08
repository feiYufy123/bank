class Admin:
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd

    def land(self):
        name = input("请输入用户名")
        passwd = input("请输入密码")
        if self.name == name and self.passwd == passwd:
            print("登录成功！")
            return True
        else:
            print("登录失败！")
            return False



# a = Admin("12","12")
# a.land()