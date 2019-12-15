number = eval(input())
a = [int(x) for x in input().split()]
swapCount = 0
passCount = 1
while a != sorted(a):
    for j in range(number-1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
            swapCount += 1
    passCount +=1
print(passCount)
print(swapCount)