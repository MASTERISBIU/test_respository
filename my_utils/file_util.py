def print_file_info(filename):
    try:
        f = open(filename,'r')
        return f.read()
    except Exception as e:
        return print("没有这个文件")



def append_file_info(filename):
    try:
        f = open(filename,'a')
        add_info = input("输入加入内容")
        f.write(add_info)
        return print(f"文件内容已加入{f.read()}")
    except Exception as e:
        print("出现异常 请检查代码")