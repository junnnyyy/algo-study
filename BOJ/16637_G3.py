def calc(a, operator, b):
    a = int(a)
    b = int(b)
    if operator == '+':
        return a+b
    elif operator == '*':
        return a*b
    else:
        return a-b


n = int(input()) # 수식의 길이
max_tran = n // 2 # 괄호를 만들수 있는 곳의 수
max_sync = n // 4 # 동시에 괄호로 묶을수 있는 식의 수
sik = list(input())
couple = []
ans = (-2) ** 31
for i in range(0, n-1, 2):
    couple.append(calc(sik[i], sik[i+1], sik[i+2]))
print(couple)
used = [0] * n
for j in couple:
    w = 0
    val = sik[w]
    while w < n:
        val = calc(val, sik[w+1], sik[w+2])
        w += 2
        if w == 2 * j:
            val = calc(j, )
            j+=1







