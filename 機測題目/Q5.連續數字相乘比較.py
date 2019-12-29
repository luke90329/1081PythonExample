times = eval(input())
for i in range(times):
    s = [int(x) for x in input().split()]
    b = []
    for j in range(len(s)-1):
        n = s[j]
        while j < len(s)-1:
            j += 1
            n *= s[j]
            b.append(n)
    print(max(b))