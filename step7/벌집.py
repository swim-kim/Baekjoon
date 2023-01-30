num = int(input())

cnt=1
count=6
count_room=1

while num > cnt:
    count_room+=1
    cnt+=count
    count+=6
print(count_room)

