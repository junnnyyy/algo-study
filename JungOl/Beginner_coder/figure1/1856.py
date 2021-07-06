h, w = map(int, input().split())

for j in range(h):
    if j % 2:
        for i in range(w+j*w, j*w, -1):
            print(i, end=' ')
        print()
    else:
        for i in range(1+j*w, w+1+j*w):
            print(i, end=' ')
        print()
