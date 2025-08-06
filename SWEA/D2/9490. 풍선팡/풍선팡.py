T = int(input())

for Tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N):        
        num = 0 # 가운데 써있는 풍선 숫자
        for j in range(M):
            total = 0
            num = arr[i][j]
            # 세로 방향 (위~아래)
            for a in range(i - num, i + num + 1):
                if 0 <= a < N:
                    total += arr[a][j]
            
            # 가로 방향 (좌~우)
            for b in range(j - num, j + num + 1):
                if 0 <= b < M:
                    total += arr[i][b]
            total =total - arr[i][j]
            if max_val <total:
                max_val=total
    print(f'#{Tc+1} {max_val}')