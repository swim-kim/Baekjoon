lst = []

for i in range(0,10):
    lst.append((int(input()))%42)
    
lst2=set(lst) 
print(len(lst2))