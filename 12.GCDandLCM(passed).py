times = eval(input())
for i in range(times):
    a, b = map(int,input().split())
    x = a*b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    lcm = int(x / a)
    print(a)
    print(lcm)