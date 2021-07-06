n = int(input())
lst = list(map(int, input().split()))
num = int(input())
yak, bae = 0, 0

for i in lst:
    if i > num:
        if not i % num:
            bae += i
    elif i == num:
       yak += i
       bae += i
    else:
        if not num % i:
            yak += i
print(yak)
print(bae)