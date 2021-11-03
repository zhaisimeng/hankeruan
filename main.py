from DBUtils import select,insert_into,update
import random
print("***************************")
print("*    中国工商银行          *")
print("*     账户管理系统         *")
print("***************************")
print(" ")
print("*1、开户                   *")
print("*2、存钱                   *")
print("*3、取钱                   *")
print("*4、转账                   *")
print("*5、查询                   *")
print("*6、欢迎下次光临            *")
print("****************************")
#初始化银行
#bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="中国工商银行"

#定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account,name,password,country,province,street,doot):

    sql="select count(*) from user"
    param=[]
    date=select(sql,param,mode="one")
    if date[0]>=100:
        return 3

    sql1="select account from user where account=%s"
    param1=[account]
    date1=select(sql1,param1,mode="one")
    if account ==date1[0]:
        return 2

    sql2="insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2=[account,name,password,country,province,street,doot,0,"2021-11-2",bank_name]
    insert_into(sql2,param2)
    return 1


#定义用户入参
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=input("请输入您的密码")
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    doot=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,street,doot)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
#存钱过程
def cunqianguocheng(account,money):

    sql="select * from user where account=%s"
    sql2="update user set money=%s where account=%s"
    param=[account]
    date=select(sql,param,mode="one")
    if account ==date[0]:
        money1=date[7]+money
        param2 = [money1,param]
        update(sql2,param2)
        return True
    else:
        return False
#存钱结果
def cunqian():
    account = int(input("请输入账号："))
    money = int(input("请输入存入余额："))
    zh=cunqianguocheng(account,money)
    if zh==True:
        print("存入成功！")
    else:
        print("用户不存在！")
#取钱结果account,name,password,country,province,steert,door,0,2021-11-2,bank_name
def quqian():
    account=int(input("请输入账号："))
    password =int(input("请输入密码："))
    jine = int(input("请输入取钱金额："))
    jieguo=quqianguocheng(account,password,jine)
    if jieguo==0:
        print("取款成功！")
    elif jieguo==1:
        print("账号不存在！")
    elif jieguo==2:
        print("密码不对！")
    elif jieguo==3:
        print("钱不够！")
# 取钱过程
def quqianguocheng(account,password,jine):
    sql="select * from user where account=%s"
    param=[account]
    date=select(sql,param,mode="one")
    if account ==date[0]:
        if password==date[2]:
            if date[7]>=jine:
                sql2="update user set money=%s where account=%s"
                money1 = date[7] - jine
                param2=[money1,param]
                update(sql2,param2)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1
#转账结果
def zhuanzhang():
    ZCaccount=input("请输入转出账户：")
    ZRaccount=input("请输入转入账户：")
    password = input("请输入转出账号的密码：")
    ZCjine = int(input("请输入转出的金额："))
    zhuanzhang=zhuanzhanguocheng(ZCaccount, ZRaccount,password,ZCjine)
    if zhuanzhang==0:
        print("转账成功！")
    elif zhuanzhang==1:
        print("账号不对！")
    elif zhuanzhang==2:
        print("密码不对！")
    elif zhuanzhang==3:
        print("钱不够！")
#转账过程
def zhuanzhanguocheng(ZCaccount,ZRaccount,password,ZCjine):
    sql = "select account from user"
    sql2 = "select password from user"
    sql3 = "select money from user"
    param = []
    date = select(sql, param)
    user_pwd = select(sql2, param)
    ZCuser_money = select(sql3, param)
    ZRuser_money = select(sql3,param)

    if ZCaccount in date and ZRaccount in date :
            for i in date:
                if ZCaccount==date[i]:
                    if password==user_pwd[i]:
                        if ZCjine<=ZCuser_money[i]:
                            for j in date:
                                if ZRuser_money[j]==ZRuser_money:
                                    ZCuser_money[i]=ZCuser_money[i]-ZCjine
                                    ZRuser_money[j]=ZRuser_money[j]+ZCjine
                                    return 0
                        else:
                            return 3
                    else:
                        return 2
    else:
        return 1
#查询过程
def chaxunguocheng(account,password):
    sql = "select account from user"
    sql2 = "select password from user"
    sql3="select account,username,country,province,street,doot,money,registerDate,bankname from user"
    param=[]
    date1=select(sql3,param)
    date=select(sql,param)
    user_pwd = select(sql2, param)

    if account in date:
        for i in date:
            if account==date[i]:
                if password==user_pwd[i]:
                    print("====================")
                    print(date1[i])
                else:
                    print("你输入的密码不正确")
    else:
        print("该用户不存在")
#输入查询内容
def chaxun():
    account=int(input("请输入查询账号："))
    password=input("请输入查询密码：")
    chaxunguocheng(account,password)
while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
    elif index ==2:
        print("存钱")
        cunqian()
    elif index ==3:
        print("取钱")
        quqian()
    elif index ==4:
        print("转账")
        zhuanzhang()
    elif index ==5:
        print("查询")
        chaxun()
    elif index ==6:
        print("下次光临")
        break
