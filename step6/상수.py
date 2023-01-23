a,b = input().split()

reverse_a=""
reverse_b=""

for i in range(0,3):
    reverse_a += a[3-(i+1)]
for j in range(0,3):
    reverse_b += b[3-(j+1)]


if int(reverse_a) > int(reverse_b):
    print(reverse_a)
else :
    print(reverse_b)