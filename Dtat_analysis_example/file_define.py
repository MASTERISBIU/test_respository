"""文件相关类文件"""
import json

#先定义一个抽象类用来做顶层设计 确定有哪些功能需要实现
from data_define import *


class FileReader:
    def read_data(self) -> list[Record]:  #将其封装 入List返回出去
        pass


class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self)->list[Record]:
        opened_file = open(self.path,'r',encoding='utf-8')
        record_list:list[Record] = []
        for line in opened_file.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        opened_file.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path


    def read_data(self)->list[Record]:
        opened_file = open(self.path,'r',encoding='utf-8')
        record_list:list[Record] = []
        for line in opened_file.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        opened_file.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("C:/Users/Administrator/Desktop/2011年1月销售数据.txt")
    list1 = text_file_reader.read_data()
    Json_file_reader = JsonFileReader("C:/Users/Administrator/Desktop/2011年2月销售数据JSON.txt")
    list2 = Json_file_reader.read_data()

    for record in list1:
        print(record)

    for record in list2:
        print(record)