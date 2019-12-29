import itertools
times = eval(input())
for i in range(times):
    a = eval(input())
    n = 1
    while a != sum: 
        for j in itertools.product('10', repeat = n):
            sum = 0
            for z in range(len(j)):
                sum += int(j[z])*((-2)**z)
            if a ==sum:
                break
        n += 1
    for _ in reversed(j):
        print(_,end='')
    print()