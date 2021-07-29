def calc(i):
    global X
    if i == N:
        while s:
            b = s.pop()
            if isinstance(b, int):
                X += b
            else:
                X = 0
                break
        return

    a = str[i]
    if a == '(' or a =='[':
        s.append(a)
    else:
        if not s:
            return
        top = s.pop()
        val = 0
        while isinstance(top, int):
            val += top
            if s:
                top = s.pop()
            else:
                return
        if top == '(' and a == ')':
            if val == 0:
                s.append(2)
            else:
                s.append(val*2)
        elif top == '[' and a ==']':
            if val == 0:
                s.append(3)
            else:
                s.append(val*3)
        else:
            return
    return calc(i+1)

str = input()
N = len(str)
X = 0
s = []
if not N % 2:
    calc(0)
print(X)