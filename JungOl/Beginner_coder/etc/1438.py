n = int(input())
arr = [[0] * 100 for _ in range(100)]
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    for yy in range(y, y+10):
        for xx in range(x, x+10):
            if not arr[yy][xx]:
                ans += 1
            arr[yy][xx] = 1
print(ans)
