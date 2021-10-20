import random
jb=2
k=0
while jb>=1:
    random1 = random.randint(1, 4)
    num = int(input("请输入猜测的数字："))
    if num==random1:
        print("恭喜你猜对了！金币+1")
        jb=jb+1
        print("现有金币数为：",jb)
        k=0
    else:
        jb=jb-1
        print("猜错了！失去一枚金币")
        print("现有金币数为：", jb)
        k = k + 1
        if k==3:
            print("你已经连续猜错3次游戏结束！")
            break
        if jb==0:
            cz=int(input("你的金币数为0，是否充值，充值输入1，不充值输入其他数字"))
            if cz==1:
                jb = int(input("请输入你要充值的金币数量："))
                print("充值成功！当前金币为：",jb)
                k=0
            else:
                print("你的金币为0，游戏结束!!!")
