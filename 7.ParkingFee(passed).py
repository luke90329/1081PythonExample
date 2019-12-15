times = eval(input())
for i in range(times):
    time = eval(input()) / 30
    total = 0
    if time > 1:
        total += 50
        time -= 2
        while time > 0:
            total += 10
            time -= 1
    print(total)