def prime(n):
    a = 2
    while a <= n ** (1/2):
        if not n % a:
            return False
        a += 1
    return True


lst = list(map(int, input().split()))
for i in lst:
    if i == 1:
        print('number one')
    elif prime(i):
        print('prime number')
    elif not prime(i):
        print('composite number')

