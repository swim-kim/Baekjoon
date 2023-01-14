hour,min = map(int,input().split())
time = int(input())

hour2 = hour*60
total = hour2+min

result1 = total+time
ovenhour = result1 // 60
ovenmin = result1 % 60

if ovenhour > 23 :
    ovenhour = ovenhour-24

print(ovenhour,ovenmin,sep=' ')

""" time_hour = time//60
time_min = time%60

if time_hour > 1 :
    if time_min+min > 60 :
        hour2 = hour+(time//60)+1
        min2 = min+(time%60) """