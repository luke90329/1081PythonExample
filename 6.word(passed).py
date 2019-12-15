for i in range(eval(input())):
    count = 0
    for i in list(input()):
        for num in ['a','e','i','o','u','y']:
            if i == num:
                count += 1
    print(count)