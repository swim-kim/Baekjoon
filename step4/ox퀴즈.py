n=int(input())

for i in range(0,n):
    
    lst = list(input())
    sum=0
    count=0 
    for k in range(0,len(lst)):   
        if lst[k]=="O":
            count+=1
            sum+=count
        else:
            count=0
    print(sum)
        