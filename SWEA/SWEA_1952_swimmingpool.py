def pay(idx):

    sel[idx] = 1



for t in range(1, int(input())+1):
    aday, amon, trimon, ayear = map(int, input().split())
    schedule = list(map(int, input().split()))
    
    sel = [0]
