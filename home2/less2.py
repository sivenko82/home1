import random
LESS1

def rand(count,min_nums,max_nums):
    ls = [random.randint(min_nums, max_nums) for i in range(count)]
    return ls
print(rand(count=int(input()),min_nums=int(input()),max_nums=int(input())))


# LESS2
pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}

cake = input("Какой торт Вы хотели бы приобрести: ").lower()
wish = input("Что Вы хотели бы уточнить: ").lower()
def x(pastry1,cake1,wish1):
    for k, v in pastry1.items():
        if k == cake1:
            if wish1 == "описание":
                print(f"Торт {k} состоит из {v[0]}")
            elif wish1 == "цена":
                print(f"Торт {k} стоит {v[1]} рублей")
            elif wish1 == "количество":
                 print(f"Торта {k} осталось {v[-1]}грамм")
            elif wish1 == "купить":
                gr = int(input("Сколько торта вам положить? "))
                print(f"К оплате {gr * v[1] / 100}")
                print(f"Торта {k} осталось {v[-1] - gr} грамм")
    return k,v
x(pastry,cake,wish)


# LESS3
def rec(x):
    if x==1:
        return 1
    return rec(x-1)*x
print(rec(5)