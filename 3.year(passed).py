import math
times = int(input())
for i in range(times):
    y,m,d = map(int,input().split())
    if m < 3:
        m = m + 12
        y = y -1
    y1 = y//100
    y2 = y%100
    w = (y2 + math.floor(y2/4) + math.floor(y1/4) - 2*y1 + 2*m + math.floor(3*(m+1)/5) + d + 1) % 7
    print(w)
    