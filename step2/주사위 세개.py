a,b,c = map(int,input().split())

if a==b and b==c and c==a :
    print(10000+a*1000)

elif a==b or b==c :
    print(1000+a*100)

elif a == c :
    print(1000+a*100)

else :
    print(max(a,b,c)*100)


#a == b or b == c 인 경우 무조건 b는 같은 눈입니다. 
#이를 바로 사용하면 되고, 주사위 세개를 던졌을 때, b가 같은 눈이 아닌 경우 단 한가지인 a == c만 따로 한번 더 고려해주면 됩니다.

""" a,b,c = map(int,input().split())

if a==b and b==c and c==a :
    print(10000+a*1000)
elif a==b and b!=c and c!=a :
    print(1000+a*100)
elif a!=b and b==c and c!=a :
    print(1000+b*100)
elif a!=b and b!=c and c==a :
    print(1000+a*100)
else :
    max = a
    if max < b:
        max =b
    if max < c:
        max =c
    print(max*100) """