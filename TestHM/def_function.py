# def intro_yourself(name,age,hobby):
#     print(f"Hello my name is {name} Im {age} years old now I like {hobby}")
#
# intro_yourself('Tom',18,'Playing guitar')
#
# def get_cirle(radius):
#     result = 3.14*(radius*radius)
#     return result
#
# print(get_cirle(10))

# def get_time_result(first_num:int,second_num:int,third_num:int):
#     result = first_num * second_num * third_num
#     return result
#
# first_num=int(input("Enter first number: "))
# second_num=int(input("Enter second number: "))
# third_num=int(input("Enter third number: "))
# print(get_time_result(first_num,second_num,third_num))



#
# def calculate_runyear(start_year:int,end_year:int):
#     a = 0
#     for year in range(start_year,end_year+1):
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             if a > 1:
#                 print()
#                 a = 0
#             print(year,end=' ')
#             a += 1
#
# start_year = int(input("Enter start year:"))
# end_year = int(input("Enter end year:"))
# calculate_runyear(start_year,end_year)
from class_design import *
student('aa','asd','3','dfa','23')