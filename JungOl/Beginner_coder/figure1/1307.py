n = int(input())
lst = [0]*n**2
cnt = n**2 -1
for i in range(n**2):
    lst[cnt] = chr((i%26) + 65)
    cnt -= 1

for i in range(n):
    for j in range(n):
        print(lst[i+n*j], end=' ')
    print()