t = int(input())

for i in range(0,t):
    arr=list(input())
    r = arr[0]
    
    for k in range(2,len(arr)):
        if k==len(arr)-1:
            print(arr[k]*int(r))
        else:
            print(arr[k]*int(r),end='')

        

