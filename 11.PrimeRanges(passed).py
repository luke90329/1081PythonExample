times = eval(input())
for i in range(times):
    a,b = input().split()
    count = 0
    for j in range(int(a),int(b)+1):
        c = 0
        if j > 1 :
            for num in range(2,j//2+1):
                if j % num == 0:
                    break
            else:
                count += 1
    print(count)