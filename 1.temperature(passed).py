times = int(input())
for i in range(times):
    a,b=map(int,input().split())
    if b == 0:
        a = float(a*(9/5)+32)
        print('%.2f' % a)
    if b == 1:
        a = float((a-32)*5/9)
        print('%.2f' % a)
