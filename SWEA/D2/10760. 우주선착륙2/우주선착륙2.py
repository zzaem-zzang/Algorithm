T = int(input())

for Tc in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    answer = 0
    for i in range(N):
        for j in range(M):
            center = matrix[i][j]
            cnt = 0

            for dx, dy in dir:
               if 0 <= i+dx < N  and 0 <= j+dy < M and  center > matrix[i+dx][j+dy]:
                    cnt +=1
            if cnt >= 4:
                answer +=1

    print(f'#{Tc+1} {answer}')