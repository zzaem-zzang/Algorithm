T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(N):
        for j in range(N):
            # + 방향 (상하좌우)
            total_plus = arr[i][j]
            for k in range(1, M):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx * k, j + dy * k
                    if 0 <= ni < N and 0 <= nj < N:
                        total_plus += arr[ni][nj]

            # x 방향 (대각선)
            total_diag = arr[i][j]
            for k in range(1, M):
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ni, nj = i + dx * k, j + dy * k
                    if 0 <= ni < N and 0 <= nj < N:
                        total_diag += arr[ni][nj]

            max_kill = max(max_kill, total_plus, total_diag)

    print(f"#{tc} {max_kill}")
