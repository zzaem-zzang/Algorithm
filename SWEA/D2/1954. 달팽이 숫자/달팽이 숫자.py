T = int(input())

for Tc in range(T):
    N = int(input())
    arr = [[0]* N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x , y = 0 , 0
    dir = 0    # 오른쪽 0 아래 1 왼쪽2 위쪽 3
    for num in range(1,(N**2)+1):
        arr[x][y] = num
        nx = x + dx[dir]
        ny = y + dy[dir]
        if  (0 <= nx < N) and (0<= ny < N) and (arr[nx][ny] == 0) :
            x , y = nx, ny
        else:
            dir = (dir + 1) % 4
            x = x + dx[dir]
            y = y + dy[dir]


    print(f'#{Tc+1}')
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=' ')
        print()
