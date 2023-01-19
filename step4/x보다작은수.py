n,x = map(int,input().split())
lst=list(map(int,input().split()))


for i in range(0,n):
    if lst[i] < x:
        print(lst[i],end=' ')
