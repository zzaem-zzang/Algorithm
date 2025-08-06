for T in range(1, 11):
    arr = []
    t = input()
    for i in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)

    max_val = 0

    for i in range(len(arr)):
        temp_sum = 0
        for j in range(len(arr[0])):
            temp_sum += arr[i][j]
        if temp_sum>max_val:
            max_val=temp_sum

    for i in range(len(arr)):
        temp_sum = 0
        for j in range(100):
            temp_sum += arr[j][i]

        if temp_sum>max_val:
            max_val=temp_sum

    diag_1 = 0
    diag_2 = 0
    for i in range(len(arr)):
        diag_1 += arr[i][i]
        diag_2 += arr[i][len(arr)-1-i]
    if diag_1> max_val:
        max_val=diag_1
    elif diag_2> max_val:
        max_val = diag_2

    print(f'#{T} {max_val}')