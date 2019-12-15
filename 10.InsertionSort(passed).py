times = eval(input())
arr = [int(x) for x in input().split()]
for i in range(1,len(arr)):
    if arr == sorted(arr):
        print('0')
        break
    count = 0
    temp = arr[i]
    j = i - 1
    while j >= 0 and temp < arr[j]:
        arr[j+1] = arr[j]
        j = j - 1
        count += 1
    arr[j+1] = temp
    print(count)