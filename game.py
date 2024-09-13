from datetime import time


def get_string(func):
    def inner():
        ss = func()
        news = ss + ".txt"
        return news
    return inner
@get_string
def hello():
    return "Hello World!"
result = hello()
print(result)


import time
def get_running_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print()
        print(end - start)
        return result
    return inner

@get_running_time
def calculate_runyear(start_year:int,end_year:int):
    a = 0
    for year in range(start_year,end_year+1):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if a > 4:
                print()
                a = 0
            print(year,end=' ')
            a += 1

calculate_runyear(100,2050)
#
#
# def get_lost_int(a_list:list):
#     total = (1 + len(a_list)+1)*(len(a_list)+1)/2
#     result = total - sum(a_list)
#     return result
#
# a_list = [4,2,3,5,6,7,8]
# print(get_lost_int(a_list))
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        arr[i], arr[i-1] = arr[i-1], arr[i]
        arr[i], arr[i+1] = arr[i+1], arr[i]
        heap_sort(arr)
        print(arr)
def greedy_algorithm(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        arr[i], arr[i-1] = arr[i-1], arr[i]
        arr[i], arr[i+1] = arr[i+1], a