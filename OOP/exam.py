from abc import ABC, abstractmethod
class Metod(ABC):

    @abstractmethod
    def convert(self):
        pass

class Name(Metod):
    def __init__(self,lastname):
        self.lastname=lastname
    def convert(self):
        a=self.lastname
        b=self.lastname[0:1]
        a="*"*len(a[1:])
        return b+a
if __name__ == '__main__':
    a=Name("Roman")
    print(a.convert())