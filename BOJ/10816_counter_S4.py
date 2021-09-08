import sys
from collections import Counter


n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))
cnt = Counter(cards)
for _ in check:
    print(cnt[_], end=' ')
