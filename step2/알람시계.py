hour,min = map(int,input().split())

if min < 45 :
    if hour == 0 :
        hour2 = 23
        min2 = 60-(45-min)
    else : 
        hour2 = hour-1
        min2 = 60-(45-min)
else :
    hour2 = hour
    min2 = min-45

print(hour2,min2, sep=' ')