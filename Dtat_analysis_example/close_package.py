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
def account_create(initial_account = 0):

    def atm(num,deposite=True):
        nonlocal initial_account
        if deposite:
            initial_account += num
            print(f"存款：+{num},账户余额：{initial_account}")
        else:
            initial_account -= num
            print(f"存款：-{num},账户余额：{initial_account}")
    return atm

atm = account_create()
atm(100)
atm(200)
atm(100,deposite=False)
