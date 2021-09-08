def second(chars):
    for i, char in enumerate(chars):
        if char in list('~!@#$%^&*()=+[{]}:?,<>/'):
            chars[i] = ''
    return chars


def third(chars):
    new_chars = ''
    for char in chars:
        if not new_chars and char == '.':
            pass
        elif char == '.' and new_chars[-1] == '.':
            pass
        else:
            new_chars += char
    return list(new_chars)


def fourth(chars):
    if chars and chars[0] == '.':
        if len(chars) >= 2:
            chars = chars[1:]
        else:
            chars = ''
    if len(chars) and chars[len(chars) - 1] == '.':
        chars = chars[:len(chars) - 1]
    return chars


def seventh(chars):
    if len(chars) <= 2:
        end = chars[len(chars) - 1]
        while len(chars) < 3:
            chars += end
    return chars


def solution(new_id):
    answer = ''
    tmp = list(new_id.lower())
    tmp = second(tmp)
    tmp = third(tmp)
    tmp = fourth(tmp)
    if not tmp:
        tmp = 'a'
    if len(tmp) >= 16:
        tmp = tmp[:15]
        tmp = fourth(tmp)
    tmp = seventh(tmp)
    answer = ''.join(tmp)
    return answer