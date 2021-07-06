import sys

sys.stdin = open("input.txt", 'r')


for t in range(1, int(input())+1):
    N = int(input())
    # 각각의 상자들의 가로, 세로, 높이 길이
    g, s, h  = map(int, input().split())

    