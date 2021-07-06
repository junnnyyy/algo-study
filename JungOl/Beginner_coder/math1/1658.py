a, b = map(int, input().split())

def get_gcd(a, b):
    if not b:
        return a
    else:
        return get_gcd(b, a % b)

gcd = get_gcd(a, b)
lcm = (a * b) // gcd

print(gcd)
print(lcm)