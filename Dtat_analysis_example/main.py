import pyecharts.charts
from pymysql import connect
from pyecharts.options import LabelOpts, InitOpts

from file_define import *
from data_define import *
from pyecharts import *
from pyecharts.charts import *
from pyecharts.globals import *
from pymysql import Connection

text_file_reader = TextFileReader("C:/Users/Administrator/Desktop/2011年1月销售数据.txt")
Json_file_reader = JsonFileReader("C:/Users/Administrator/Desktop/2011年2月销售数据JSON.txt")
Jan_data:list[Record] = text_file_reader.read_data()
Feb_data:list[Record] = Json_file_reader.read_data()
#将两个月份数据合并为一个文件来存储
all_data:list[Record] = Jan_data + Feb_data
#构建SQL连接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='mysql',
    autocommit = True
)
#获得游标对象
cur = conn.cursor()
#选择数据库
conn.select_db('Orders')
#组织SQL语句
for record in all_data:
    sql = f"insert into python_data_import values ('{record.date}','{record.order_id}','{record.money}','{record.province }')"
    cur.execute(sql) #执行SQL语句

#关闭链接
cur.close()
#开始进行数据计算
# data_dict = {}
# for record in all_data:
#     if record.date in data_dict.keys(): #当前日期已经有了 对金额做累加
#         data_dict[record.date] += record.money
#         pass
#     else:
#         data_dict[record.date] = record.money
# bar = pyecharts.charts.Bar(init_opts=InitOpts(theme=ThemeType.DARK))
# bar.add_xaxis(list(data_dict.keys()))
# bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
# bar.render("每日销售额柱状图.html")
# print(data_dict)