times = eval(input())
for i in range(times):
    a,b = map(int,input().split())
    a = str(a)
    ra = a[::-1]
    if b == 0:
        al = a + ra
    else:
        al = a + ra[1:]
    print(al)