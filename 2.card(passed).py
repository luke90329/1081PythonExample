times = int(input())
for i in range(times):
    total = 0
    number = input()
    for i in range(1,9):
        a = int(number[(i-1)*2])*2
        e = int(number[i*2-1])
        if a/10 >= 1:
            a = (a//10 + a%10)
        total = total + a + e
    if total % 10 == 0:
        print('Verified')
    else:
        print('Unverified')
