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