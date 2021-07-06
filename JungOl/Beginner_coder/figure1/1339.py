n = int(input())
if not n % 2 or n > 100 or n <= 0:
    print('INPUT ERROR')
else:
    lst = [0] * n ** 2
    for i in range(n ** 2):
        lst[i] = chr((i % 26) + 65)
    lst = lst[:((n // 2) + 1) ** 2]
    arr = [[''] * n for _ in range(n)]

    k = len(lst)-1
    for i in range(n):
        for j in range(n - i - 1, i - 1, -1):
            arr[j][i] = lst[k]
            k -= 1

    for _ in range(n):
        print(*arr[_])
