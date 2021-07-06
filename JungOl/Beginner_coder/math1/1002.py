def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)


n = int(input())
lst = list(map(int, input().split()))
lcm = gcd = lst[0]

for i in range(1, n):
    gcd = get_gcd(gcd, lst[i])
    lcm = (lcm * lst[i]) // get_gcd(lcm, lst[i])

print(gcd, lcm)