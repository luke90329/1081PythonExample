number = eval(input())
a = [int(x) for x in input().split()]
while len(a) > 1:
    t = 0
    index = 0
    for i in range(len(a)):
        if a[i] > t:
            t = a[i]
            index = i
    a[index] = a[len(a)-1]
    del a[len(a)-1]
    if a == sorted(a):
        break
    print(index)