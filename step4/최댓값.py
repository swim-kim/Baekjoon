lst=[]
for i in range(0,9):
    lst.append(int(input()))
print(max(lst))
for i in range(0,9):
    if lst[i]==max(lst):
        print(i+1)