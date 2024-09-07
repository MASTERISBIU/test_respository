# my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcastt','best']
#
# my_set=set()
#
# for i in my_list:
#     my_set.add(i)
# print(my_set)

# Python容器-作业
# 总结题
# 请使用xmind思维导图对本章节知识做个知识总结。
# 简答题
# 题目1(简答题)
# 题干
# 如何创建字符串？字符串切片操作的语法格式是怎样的，能举例子说明吗？
# a = 'abc'
# a[]
# a[0:2:1]
# 考察知识点
# 字符串
# 切片
# 题目2(简答题)
# 题干
# 请使用自己的话来说一说Python容器字符串、列表、元组、字典的使用与特点。
# 考察知识点
# Python容器
# 字符串
# 列表 列表可以增删改查 但是还是那个原列表 不会生成新的列表 存放的元素 类型可以不一样
# 元组 不能增删改 只能查 元组的数据对换
# 字典 kv键值对
# 各个类型的特点
# 实操题
# 题目3（实操题）
# 题干
# 比如，6班的学生有：张三、李四、王五、钱六，从键盘上录入一个学生姓名，检验是否是6班的学生。若是6班的学生，就输出：6班学生，欢迎你；否则，输出：非6班学生，非诚勿扰。
# class_six=["张三","李四","王五","钱六","赵七","郑八"]
# class_mate = input("告诉我你要找谁")
# if class_mate in class_six:
#     print(f"确实他在这个班里，他的位置是{class_six.index(class_mate)}")
# else:
#     print("兄弟找错地方了")
# 考察知识点
# in关键字
# if语句
# 题目4（实操题）
# 题干
# 请对字符串"abcdefgABCDEFG"进行如下切片操作：
my_str="abcdefgABCDEFG"
# a.获取第1个位的元素值，获取下标为5的元素值；
print(my_str[0])
print(my_str[5])
# b.截取下标值[3, 7)的内容；
print(my_str[3:7])
# c.截取下标值5到结尾的内容；
print(my_str[5:])
# d.截取下标值1到倒数第3个的内容；
print(my_str[1:-3])
# e.截取起始处到下标值为9的内容；
print(my_str[:9])
# f.截取下标2到12且每隔3个字母截取一下内容。
print(my_str[2:12:3])
# 考察知识点
# 字符串
# 切片
# 题目5（实操题）
# 题干
# 定义一个列表，用于存放手机品牌信息，例如小米、华为、OPPO、苹果、荣耀等，要求：
mobile_list = ['小米','华为','OPPO','苹果','荣耀']
# （1）访问元素华为，获取列表总长度；
print(mobile_list.index('华为'))
print(len(mobile_list))
# （2）使用for循环遍历手机品牌列表，并输出所有元素；
for i in mobile_list:
    print(i,end=' ')
# （3）使用while循环遍历手机品牌列表，并输出所有元素。
print()
j = 0
while j < len(mobile_list):
    print(mobile_list[j],end=' ')
    j += 1
# 考察知识点
# 列表
# 循环遍历
# 访问元素
# 题目6（实操题）
# 题干
# 请使用字典类型来表示一台电脑的信息，例如有电脑品牌、价格、电脑屏幕尺寸、系统版本等，并单独获取品牌值、价格值。并给电脑信息字典做如下操作：
my_dict = {'screen':24, 'price':6500, 'system':'windows11','brand':'HP'}
# （1）查看字典的屏幕尺寸值；
print(my_dict['screen'])
# （2）修改价格值为8999；
my_dict['price'] = 8999
print(my_dict['price'])
# （3）给字典添加电脑所属类型，如游戏本、或商务本、或轻薄本等；
my_dict['computer_type']='游戏本'
print(my_dict)
# （4）删除电脑的系统版本元素。
my_dict.pop('system')
print(my_dict)
# 考察知识点
# 字典
# 字典的使用