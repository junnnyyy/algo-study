a = int(input())
b = int(input())
c = int(input())

cnt = [0] * 10
mul = str(a * b * c)

for i in mul:
    cnt[int(i)] += 1

for _ in range(10):
    print(cnt[_])
