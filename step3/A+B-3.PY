count = int(input())
list=[]
for i in range(1,count+1):
    a,b = map(int,input().split())
    i =+ 1
    list.append(a+b)

for i in range(0,count):
    print(list[i])