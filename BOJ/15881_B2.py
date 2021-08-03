n = int(input())
things = input()
res = 0
i = 0
while i < n:
    if things[i] == 'p' and things[i:i+4] == 'pPAp':
        i += 4
        res += 1
    else:
        i += 1
print(res)
