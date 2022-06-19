class BeautySalonMixin:
    price=20
    def __init__(self,open,close):
        self.open=open
        self.close=close
    def manic(self):
        a=int(BeautySalonMixin.price)
        return f"маник стоит {a+(a*0.20)} руб"
    def haircut(self,long):
        wor=int(BeautySalonMixin.price)
        if long<30:
            return f"стрижка стоит {wor+(wor*0.20)}"
        elif 30<=long<=50:
            return f"стрижка стоит {wor+(wor*0.50)}"
        else:
            return f"стрижка стоит {wor+(wor*0.80)}"

    def salon_opening_hours(self, time):
        if self.close> time > self.open:
            return "салон открыт"
        return "салон закрыт"

    def set_timework(self, timeopen, timeclose):
        self.open = timeopen
        self.close = timeclose

if __name__ == '__main__':
    a=BeautySalonMixin(10,20)
    print(a.haircut(int(input())))