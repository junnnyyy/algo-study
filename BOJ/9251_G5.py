a = input()
b = input()
lcs = [0 for _ in range(len(b)+1)]
max_ans = min(len(a), len(b))
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            lcs[j] = min(max(lcs[j], lcs[j-1] + 1), j+1)
        else:
            lcs[j] = max(lcs[j], lcs[j-1])
        if lcs[j] == max_ans:
            break
    print(lcs)
print(max(lcs))


'''
XXXXXF
XFXXXQ
ACAYKP
CAPCAK
qsdferrfgtfsawfsefeesgdtdrgthyytfgfddsdawdwd
efvs
'''