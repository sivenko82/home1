class Dog:
    def __init__(self, name, age, master):
        self.name=name
        self.age=age
        self.master=master
    def jump(self):
        return   f"прыжок {self.name} на м"
    def run(self,):
        return f'сокрость бега {self.name} км в ч '
    def birthday(self,birthday):
         return  self.age+1 ,"возраст"
    def bark(self):
        return f" лаять"

class Cat:
    def __init__(self,name,age,master):
        self.name=name
        self.age=age
        self.master=master
    def run(self,run):
        return "кошка бежит"
    def jump(self,jump):
        return "прыжок"
    def birthday(self,birthday):
         return  self.age+1 ,"возраст"
    def sleep(self,sleep):
        return f"{sleep} спит "
    def meow(self):
        return f"мяу"

class Parrot:

    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master
    def run(self, run):
        return "попугай бежит"
    def jump(self, jump):
        return " попугай прыжок"
    def birthday(self, birthday):
        return self.age + 1, "возраст попугая"
    def sleep(self,sleep):
        return f"{sleep} спит "
    def fly(self):
        return f"летать"
class Pet(Dog,Cat,Parrot):
    def __init__(self,master, age, name ):
        super().__init__(name, age, master)
    def run(self, run):
        return "бежит"
    def jump(self, jump):
        return "  прыжок"
    def birthday(self, birthday):
        return self.age + 1, " попугая"
    def sleep(self,sleep):
        return f"{sleep} спит "
    def Del(self):
        del self.name,self.age,self.master

if __name__=="__main__":
    dogs=Pet(60,12,"vita")
    print(dogs.Del())
    print(dogs.bark()  ,dogs.fly(),dogs.meow(),sep="\n")