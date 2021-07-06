import math
N = int(input())
arr = []
for i in range(1, int(N**(1/2))+1):
    if not N % i:
        arr.append(i)
        if i != N//i:
            arr.append(N//i)

print(*sorted(arr))