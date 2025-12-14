from collections import deque

N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]

def find(x,y):
    visited[x][y] = True
    cnt = 0 
    q = deque()
    q.append((x,y))
    direction = ([0,1],[0,-1],[1,0],[-1,0])

    while q:
        a, b = q.popleft()
        if graph[a][b] == 'P':
            cnt += 1

        for dx, dy in direction:
            nx = a + dx
            ny = b + dy
            if 0<= nx < N and 0<= ny < M:
                if not visited[nx][ny] and graph[nx][ny] != 'X':
                    q.append([nx, ny])
                    visited[nx][ny] = True
    return cnt
graph = []

for _ in range(N):
    lst = list(input())
    graph.append(lst)
    

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            
            C = find(i,j)

if C == 0:
    print('TT')
else:
    print(C)


