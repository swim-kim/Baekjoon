n = int(input())
lst = list(map(int,input().split()))
lst2=[]
m=max(lst)

for i in range(0,n):
    lst2.append(lst[i]/m*100)

print(sum(lst2)/n)

