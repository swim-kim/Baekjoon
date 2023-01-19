a = int(input())
a2 =a

n =0
new =0
while True:
    b = a//10+a%10
    new = (a%10)*10+b%10
    a=new
    n=n+1
    if new == a2:
        print(n)
        break
   