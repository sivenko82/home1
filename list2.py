days = { 1:'Sun', 2:'Mon', 3:'Tue', 4:'Wed', 5:'Thu', 6:'Fri', 7:'Sat'}
with open("text.txt","a") as f :
    for i,y in days.items():
        f.write(str(i)+":")
        f.write(str(y)+"\n")

with open("text.txt") as f:
    key={}
    for i in f.readlines():
            key[i[0:1]]=i[2:5]
    print(key)

sett={1,2,3,4,5,6,7,8}
with open("text2.txt", "a") as f:
    for i in sett:
        f.write(str(i)+"\n")

with open("text2.txt") as f:
    sett=set()
    for i in f.read():
        sett.add(str(i))
    sett.remove("\n")
print((sorted(sett)))

say=input().split()
with open("text3.txt","w") as f :
    for i in say:
       f.write((i)+"\n")

a=[5, True,'abc']
with open("text3.txt","a") as f :
    for i in a:
        f.write(str(i)+"\n")

a=[1,2,3,4,5,6,7,8,9,0]
with open("text3.txt","a") as f:
    for i in a:
        if i%2!=0:
            f.write(str(i)+"\n")
