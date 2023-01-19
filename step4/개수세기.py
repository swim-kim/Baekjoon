n = int(input())
lst = list(map(int,input().split()))
v = int(input())
count=0

for i in range(0,n):
    if lst[i]==v:
        count=count+1
print(count)    
