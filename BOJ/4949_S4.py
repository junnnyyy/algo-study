string = list(input())
while string[0] != '.':
    ans = 'yes'
    s = []
    while string:
        char = string.pop()
        if char == ')' or char == ']':
            s.append(char)
        elif char == '(':
            if s and s[-1] == ')':
                s.pop()
            else:
                ans = 'no'
                break
        elif char =='[':
            if s and s[-1] == ']':
                s.pop()
            else:
                ans = 'no'
                break
    if s:
        ans = 'no'
    print(ans)
    string = list(input())



