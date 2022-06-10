

class Dog:
    def __init__(self, height, weight, name, age):
        self.height=height
        self.weight=weight
        self.name=name
        self.age=age
    def jump(self,ju):
        return   f"прыжок {self.name} на {ju}м"
    def run(self,ru):
        return f'сокрость бега {self.name} {ru}км в ч '
    def bark(self,ba):
        return f"{self.name} любит лаять"
    def stat(self):
        return f"характеристики собаки :{self.height}:рост " \
               f"  {self.weight} :масса" \
               f"  {self.name}: кличка" \
               f"  {self.age} :возраст "
    def change_mane(self):
        self.name1=input("введите новое имя:")
        self.name=self.name1
        print(f"новое имя собаки:{self.name1}")
if __name__=="__main__":
    dogs=Dog(60,12,"bob",4)
    print(dogs.jump(1),dogs.run(40),dogs.bark(0),sep="\n")
    print(dogs.stat())
    print(dogs.change_mane())