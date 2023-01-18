total = int(input())
count = int(input())
lst = []
sum = 0

for i in range(0,count):
    a,b = map(int,input().split())
    lst.append(a*b)

for i in range(0,count):
    sum = sum+lst[i]
if sum == total:
    print("Yes")
else :
    print("No")
