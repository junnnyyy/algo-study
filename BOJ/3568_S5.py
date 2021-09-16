chars = input()
lst = chars.split()
cnt = len(lst)
common_var_type = lst[0]
for i in range(1, cnt):
    var_name = ''
    sub_var_type = ''
    j = 0
    while j < len(lst[i])-1:
        if 'A' <= lst[i][j] <= 'Z' or 'a' <= lst[i][j] <= 'z':
            var_name += lst[i][j]
            j += 1
        else:
            if lst[i][j] == '[':
                sub_var_type = '[]' + sub_var_type
                j += 2
            else:
                sub_var_type = lst[i][j] + sub_var_type
                j+=1
    var_type = (common_var_type + sub_var_type).strip()
    print(var_type, var_name + ';')
