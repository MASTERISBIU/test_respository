class Dog:
    @classmethod
    def eat(cls):
        print("Eating")


    @staticmethod
    def drink():
        print("Drinking")


Dog.drink()