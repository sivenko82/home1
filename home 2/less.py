
def sum(*naus):
    for i in naus:
        suma =0
        while i > 0:
            digit = int(i) % 10
            suma = suma + digit
            i = int(i) // 10
        print(suma)
print(sum(965, 582, 23, 8 ,695210))


def f(x):
    if x<=-2:
        f=1-(x+2)**2
    elif x>-2 and x<=2:
        f=-(x/2)
    elif x>2:
        f=(x-2)**2+1
    return f
print(f(4.5))


a=input().split()
def f(x):
    for i in x:
        if int(i)%2==0:
            a1=int(i)//2
            print(a1)

print(f(a))