n = 1
while n != 0:
    n = int(input())
    if not n:
        break
    a = str(n)
    b = ''
    total = 0
    for i in range(len(a)-1, -1, -1):
        b += a[i]
        total += int(a[i])
    print(int(b), total)