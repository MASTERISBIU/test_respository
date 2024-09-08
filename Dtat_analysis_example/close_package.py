"""
演示Python闭包特性
"""

#简单闭包
# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
#
#
# fn1 = outer("Hello")
# fn1("World")

#使用Nonlocal关键字修改outer变量

# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#     return inner
#
#
# fn2 = outer(10)
# fn2(10)
# fn2(10)
# fn2(10)

#利用闭包实现ATM小案例
def account_create(func):
    def atm(*args, **kwargs):
        result = func(*args, **kwargs)
        initial_account = result[0]
        num = result[1]
        deposite = result[2]
        if deposite:
            initial_account += num
            print(f"存款：+{num},账户余额：{initial_account}")
        else:
            initial_account -= num
            print(f"存款：-{num},账户余额：{initial_account}")
        return initial_account
    return atm

@account_create
def get_money(num, deposite=True):
    money = 100
    return money, num, deposite

result = get_money(100, deposite=True)
print(result)