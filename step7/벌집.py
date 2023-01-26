num = int(input())
i=0
if num==1:
    print(1)
elif num>=2 and num<=7:
    print(2)
else:
    if 2<num%6 and num%6<7:
        print(int(num/6))