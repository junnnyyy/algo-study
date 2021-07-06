n, m = map(int, input().split())

for h in range(n):
    for w in range(1, m+1):
        print(w+m*h, end=' ')
    print()
