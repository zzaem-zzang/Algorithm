T = int(input())

for Tc in range(T):
    num = int(input())
    arr = [ [0]* num for _ in range(num)]

    for i in range(num):
        for j in range(num):
            if i == j or j ==0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{Tc+1}')
    for row in range(num):
        for col in range(num):
            if arr[row][col] != 0:
                print(arr[row][col], end=' ')
        print()  