def calc(nums, lst):
    # print('calc start', lst)
    ans = nums[0]
    for i in range(len(lst)):
        if lst[i] == 0:
            ans += nums[i+1]
        elif lst[i] == 1:
            ans -= nums[i+1]
        elif lst[i] == 2:
            ans *= nums[i+1]
        else:
            if ans < 0:
                ans = -(abs(ans)// nums[i+1])
            else:
                ans //= nums[i+1]
    return ans

# 같은것이 많이 있는 순열일때는 직접 구현하는게 Itertools 보다 더 빠르다.
def dfs(S, op):
    global max_val, min_val
    # 식이 만들어졌으면 계산 후 비교
    if len(S) == N - 1:
        val = calc(nums, S)
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    else:
        for j in range(4):
            if op[j]:
                S.append(j)
                op[j] -= 1
                dfs(S, op)
                S.pop()
                op[j] += 1


N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
max_val = -(10 ** 10)
min_val = 10 ** 10
dfs([], op)
print(max_val)
print(min_val)