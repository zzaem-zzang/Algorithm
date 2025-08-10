T = int(input())

for Tc in range(1,T+1):
    arr = []
    N, M = map(int, input().split())
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    total = 0
    for i in range(N):
        for j in range(M):
            up = arr[i+1][j] if i+1 < N else 0
            down = arr[i-1][j] if i-1 >= 0 else 0
            left = arr[i][j-1] if j-1 >= 0 else 0
            right = arr[i][j+1] if j+1 <M else 0
            sub_set = up + down + left + right + arr[i][j]


            if sub_set > total:
                total = sub_set
    print(f"#{Tc} {total}")