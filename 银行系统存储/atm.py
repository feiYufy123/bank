from user import User
from card import Card
import random
class Atm:
    def __init__(self):
        self.dict1 = {}

    def open(self):
        name = input("请输入名字")
        idc = input("请输入身份证号")
        phone = input("请输入手机号")
        passwd1 = input("请输入密码")
        passwd2 = input("请重新输入密码")
        if passwd2 == passwd1:
            money = int(input("输入金额"))
            if money >= 10:
                cardNum = random.randint(100000,999999)
                print("开户成功！姓名%s 金额%d,卡号%d" %(name,money,cardNum))
                card = Card(cardNum,passwd2,money)

                u =User(name,idc,phone,card)
                self.dict1[cardNum] = u

                return True
            else:
                print("金额过低，开户失败！")
                return False
        else:
            print("2次输入密码不一致，开户失败")
            return False

    '''
        1.先输入卡号
        2.检测卡号是否存在
        3.检测卡号是否锁定
        4.输入密码(3次机会)
        5.显示信息
        :return:
        '''
    def search(self):
        cardNum = int(input("输入卡号"))
        d = self.dict1.get(cardNum)
        if d == None:
            print("不存在此卡")
            return False
        else:
            print("继续执行")
            if d.card.lock == True:
                print("卡已经被锁")
                return False
            else:
                for i in range(3):
                    passwd = input("输入密码")
                    if passwd == d.card.passwd:
                        print("剩余金额%d"%d.card.money)
                        return True
                    else:
                        print("输入密码错误")
                else:
                    print("is lock")
                    d.card.lock = True


    def qu(self):
        cardNum = int(input("输入卡号"))
        d = self.dict1.get(cardNum)
        if d == None:
            print("不存在此卡")
            return False
        else:
            print("继续执行")
            if d.card.lock == True:
                print("卡已经被锁")
                return False
            else:
                for i in range(3):
                    passwd = input("输入密码")
                    if passwd == d.card.passwd:
                        money = int(input("请输入要取的金额"))
                        d.card.money -= money
                        print("剩余金额%d"%d.card.money)
                        return True
                    else:
                        print("输入密码错误")
                else:
                    print("is lock")
                    d.card.lock = True


    def cun(self):
        cardNum = int(input("输入卡号"))
        d = self.dict1.get(cardNum)
        if d == None:
            print("不存在此卡")
            return False
        else:
            print("继续执行")
            if d.card.lock == True:
                print("卡已经被锁")
                return False
            else:
                for i in range(3):
                    passwd = input("输入密码")
                    if passwd == d.card.passwd:
                        money = int(input("请输入要存的金额"))
                        d.card.money += money
                        print("剩余金额%d" % d.card.money)
                        return True
                    else:
                        print("输入密码错误")
                else:
                    print("is lock")
                    d.card.lock = True

    def zhuan(self):
        cardNum = int(input("请输入自己卡号"))
        cardNum1 = int(input("请输入对方卡号"))
        d = self.dict1.get(cardNum)
        d1 = self.dict1.get(cardNum1)
        if d == None or d1 == None:
            print("不存在此卡")
            return False
        else:
            print("继续执行")
            if d.card.lock == True:
                print("卡已经被锁")
                return False
            else:
                for i in range(3):
                    passwd = input("输入密码")
                    if passwd == d.card.passwd:
                        money = int(input("请输入要转的金额"))
                        d.card.money -= money
                        d1.card.money += money
                        print("剩余金额%d" % d.card.money)
                        return True
                    else:
                        print("输入密码错误")
                else:
                    print("is lock")
                    d.card.lock = True


    def gai(self):
        cardNum = int(input("输入卡号"))
        d = self.dict1.get(cardNum)
        if d == None:
            print("不存在此卡")
            return False
        else:
            print("继续执行")
            if d.card.lock == True:
                print("卡已经被锁")
                return False
            else:
                for i in range(3):
                    passwd = input("输入密码")
                    if passwd == d.card.passwd:
                        c = input("请输入新密码")
                        d.card.passwd = c

                        return True
                    else:
                        print("输入密码错误")
                else:
                    print("is lock")
                    d.card.lock = True


    def suo(self):
        cardNum = int(input("输入卡号"))
        d = self.dict1.get(cardNum)
        if d == None:
            print("不存在此卡")
            return False
        else:
            print("继续执行")
            idc = input("输入身份证号")
            passwd = input("请输入密码")
            if idc == d.idc and passwd == d.card.passwd:
                d.card.lock = True
                print("卡已经被锁")
            else:
                return True


    def jie(self):
        cardNum = int(input('请输入自己的卡号：'))
        d = self.dict1.get(cardNum)
        if d == None:
            print("卡号不存在，解锁失败。。。")
            return False
        if d.card.lock == False:
            print("卡未锁定，不需要解锁。。。")
            return False
        idc = input("请输入您的身份证号")
        if idc != d.idc:
            print("身份证号错误")
            return False
        d.card.lock = False
        print("解锁成功")


    def xiao(self):
        cardNum = int(input('请输入自己的卡号：'))
        d = self.dict1.get(cardNum)
        if d == None:
            print("卡号不存在，销户失败。。。")
            return False

        idc = input("请输入您的身份证号")
        if idc != d.idc:
            print("身份证号错误")
            return False
        self.dict1.pop(cardNum)
        print("销户成功！")

    def esc(self):
        exit()







