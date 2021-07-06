for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0 for _ in range(N)] for __ in range(N)]
    
    print(dist)