def starring(n):
    if n == 3:
        star = '*'
        stars = star * 3 + '\n' + star + ' ' + star + '\n' + star * 3
        return stars
    else:
        star = starring(n//3)
        stars = star * 3 + '\n' + star + ' ' + star + '\n' + star * 3
        return stars

N = int(input())
print(starring(N))
