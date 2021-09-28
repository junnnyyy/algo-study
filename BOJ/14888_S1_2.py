import itertools

def calc(nums, lst):
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

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
max_val = -(10 ** 10)
min_val = 10 ** 10
op_lst = [i for i in range(len(op)) for j in range(op[i])]

for i in itertools.permutations(op_lst, N-1):
    val = calc(nums, i)
    max_val = max(max_val, val)
    min_val = min(min_val, val)

print(max_val)
print(min_val)