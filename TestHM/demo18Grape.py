#一串葡萄个数位置 第三颗葡萄有不明生物 我只能吃10颗葡萄 写循环模拟吃葡萄

grapes_nums = int(input("告诉我你有几颗葡萄"))
#总共吃10颗
for i in range(1,grapes_nums+1):
    #第三颗和三的倍数
    if i % 3 == 0:
        print(i)
        print("你已经变异")
        break
    else:
        print(i)
        print("你吃饱了么")

