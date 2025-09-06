from collections import deque

def bfs(a,b):
    distance[a][b]=1
    queue = deque()
    queue.append((a,b))
    visited[a][b]= True
    while queue:
        a,b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<= nx <N and 0<= ny < M and not visited[nx][ny]:
                if maze[nx][ny] ==1:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[a][b] +1
    return distance[N-1][M-1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
distance =[[0]* M for _ in range(N)]
maze = [list(map(int, input().strip())) for _ in range(N)]
result = bfs(0,0)
print(result)