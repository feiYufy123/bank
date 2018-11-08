'''
主程序
管理员类：
    属性：管理员的名字和密码
    行为：登陆
用户类：
    属性：姓名、身份证号、手机号、卡
    行为：
卡类：
    属性：卡号、密码、余额、是否锁定
    行为：
ATM类：
    属性：列表(字典)---所有的用户
    行为：开户、查询、讯款、取款。。。
'''
from atm import Atm
from admin import Admin
atm = Atm()

def show():
    print("""**************欢迎来到登录页面**************
                       ************************************
                       *       开户（1）   查询（2）       *
                       *       取款（3）   存款（4）       *
                       *       转账（5）   改密（6）       *
                       *       锁定（7）   解锁（8）       *
                       *       销户（9）   退出（t）       *
                       ************************************
                """)
    bh = input("请输入编号")
    if bh == "1":
        atm.open()
    if bh == "2":
        atm.search()
    if bh == "3":
        atm.qu()
    if bh == "4":
        atm.cun()
    if bh == "5":
        atm.zhuan()
    if bh == "6":
        atm.gai()
    if bh == "7":
        atm.suo()
    if bh == "8":
        atm.jie()
    if bh == "9":
        atm.xiao()
    if bh == "t":
        atm.esc()


a = Admin("12","12")
for i in range(3):
    isok = a.land()
    if isok == True:
        while True:
            show()




















