from collections import deque

def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append((i, j))
    while q:
        X, Y = q.popleft()
        for nX, nY in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx = nX+X
            ny = nY+Y
            if 0<= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[X][Y] + 1
                q.append((nx, ny))



M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

bfs()

result = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        result = max(result, tomato[i][j])
print(result-1)
        


