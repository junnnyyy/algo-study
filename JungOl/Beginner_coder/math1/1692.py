a = int(input())
b = input()
ans = [0] * 3

for i in range(3):
    c = a * int(b[3-i-1])
    ans[i] = a * int(b[3-i-1]) * (10 ** i)
    print(c)
print(sum(ans))