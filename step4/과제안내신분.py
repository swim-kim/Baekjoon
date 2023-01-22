lst=[]

for i in range(1,31):
    lst.append(i)

for i in range(0,28):
    lst.remove(int(input()))

print(min(lst),max(lst))





