# f=open('C:/Users/Administrator/Desktop/test.txt','r',encoding='utf8')
# # print(f.read(10))
# for line in f:
#     print(line)
#
# f.close()
try:
    f = open('C:/Users/Administrator/Desktop/test1.txt', 'r', encoding='utf8')
    print(f.read())
    f.close()
except:
    print("出现异常 因为文件不存在")
    f = open('C:/Users/Administrator/Desktop/test1.txt', 'w', encoding='utf8')
    f.write("你好啊")                         