times = eval(input())
for i in range(times):
    a = list(input())
    s = set()
    for i in range(len(a)-1):
        s.add((a[i]+a[i+1]).strip())
    if len(a) <= 3:
        print('0')
    else:
        print(len(s))
        print(s)