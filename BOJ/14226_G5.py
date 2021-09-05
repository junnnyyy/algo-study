n = int(input())
lst = [val for val in range(n+1)]
# lst[idx] 는 1,2,2,2,2,2,2만했을때 idx길이 인 이모티콘을 만드는데 걸리는 시간
for i in range(1, n+1):
    x = i//2
    while x >=2:
        if not i%x and not i%2:
            lst[i] = min(lst[i], lst[i//x] + x)
        elif not i%x and i%2:
            lst[i] = min(lst[i], lst[(i + 1) // 2] + 3, lst[i//x] + x)
        x -= 1
print(lst[n])