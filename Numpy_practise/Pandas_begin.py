import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from sqlalchemy import create_engine
from sqlalchemy.types import *

data1 = pd.read_excel("C:/Users/hp/Desktop/python.xlsx")
df = pd.DataFrame(data1)
print(df[['类型']].rename(columns={'类型':'种类'}))
# a=Series(data= [1,2,3,4])
# print(a)
# b=Series(data={'A':1,'B':2,'C':3})
# print(b)
#
# """
# -Series 的索引
#     -隐式索引 默认形式的索引（0，1，2）
#     -显示索引 自定义的索引 可以通过 Index参数设置显示索引
#     -series是一个一维数据源 无法存放多维数据
# """
# c = Series(data=np.random.randint(0,100,size = (3,)),index=['A','B','C'])
# print(c)
# d = DataFrame(data = np.random.randint(0,100,size=(5,6)))
# print(d)
# """
# DataFrame进行索引操作
# """
# #对列进行索引
# # d1 = d[1]
# # print(d1)
# # d2 = d[[1,2,3]]
# # print(d2)
#
# #索引取行
#
# d3 = d.loc[1]
# print(d3)