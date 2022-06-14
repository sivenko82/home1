class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self,):
        return f"бежит{self.name}"
    def jump(self,):
        return "  прыжок"
    def birthday(self,):
        return self.age + 1, " возраст"
    def sleep(self,):
        return f"{self.name} спит "


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name,age,master)
    def bark(self):
        return f" лаять"
if __name__=="__main__":
    dogs=Dog("BOB",12,20)
    print(dogs.run(),dogs.bark(),dogs.jump(),dogs.birthday(),dogs.sleep(),sep="\n")


class Cat(Pet):
    def __init__(self, name, age, master):
        super().__init__(name,age,master)
    def meow(self):
        return f"мяу"
if __name__=="__main__":
    dogs=Cat("Catt",2,222)
    print(dogs.run(),dogs.meow(),dogs.jump(),dogs.birthday(),dogs.sleep(),sep="\n")


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name,age,master)
    def fly(self):
        return f"летать"
if __name__=="__main__":
    dogs=Parrot("Kesha",14,50)
    print(dogs.run(),dogs.fly(),dogs.jump(),dogs.birthday(),dogs.sleep(),sep="\n")