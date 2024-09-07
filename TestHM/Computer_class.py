class computer:
    def __init__(self,brand,model,year,color,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
        self.price=price

    def coding(self):
        print("I can coding")

    def video(self):
        print("I can video")



class bigdata_engineer:
    def __init__(self,job,salary_level):
        self.job=job
        self.salary_level=salary_level

    def coding_everyday(self):
        print("I can coding everyday")

    def __str__(self):
        return f"my job is {self.job},and my salary level is {self.salary_level}"

bigdata_engineer=bigdata_engineer(job='python',salary_level=100)
print(bigdata_engineer)
bigdata_engineer.coding_everyday()


class running_student:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def run_onetime(self):
        self.weight -= 0.5
        return self.weight

    def crazy_eat_drink(self):
        self.weight += 2
        return self.weight

    def __str__(self):
        return f"my name is {self.name},and my weight is {self.weight}"


student1 = running_student('小芳',100)
student1.run_onetime()
student1.run_onetime()
student1.run_onetime()
student1.run_onetime()
student1.run_onetime()
student1.crazy_eat_drink()
print(student1)


class mi_computer:
    def __init__(self,brand,model,year,color,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def playing_movies(self,movie_name):
        print(f"{self.brand}电脑播放{movie_name}")



computer1 = mi_computer("小米","su7",'2024','white','298000')
computer1.playing_movies("葫芦娃")

computer2 = mi_computer("苹果","macpro16",'2024','white','29800')
computer2.playing_movies("变形金刚")
