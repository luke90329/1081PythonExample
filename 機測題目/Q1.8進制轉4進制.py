times = eval(input())
for i in range(times):
    num = input()
    n = 0
    sum = 0
    for j in num[::-1]:
        sum += (8**(n))*int(j)
        n += 1
    b =''
    while sum >= 4:
        b += str(sum % 4)
        sum = (sum-(sum % 4))//4
    b += str(sum)
    print(b[::-1])
