times = eval(input())
for i in range(times):
    s = [2,3,5,7,11]
    a = eval(input())
    sum = 1
    for j in range(5):
        if s[j] != a:
            sum *= 1/s[j]
        else:
            sum *= 1/s[j]
            break
    print('%.3f' % round(sum,3))