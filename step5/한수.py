x = int(input())
count =0


def han(n):
   n=str(n)
   if (int(n[1])-int(n[0]))==(int(n[2])-int(n[1])):
        return True
   else :
        return False


for i in range(0,x):
    if i+1 < 100 :
        count+=1
    elif han(i+1):
        count+=1
    
print(count)
