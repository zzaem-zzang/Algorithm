from collections import deque
# 0은 통로  1은 벽 2는 출발 3은 도착

def bfs(maze, start, N):
    queue = deque()
    visitied = [[False] * N for _ in range(N)]
    x, y = start
    visitied[x][y] = True
    cnt = 0
    queue.append([x,y,cnt])
    
    while queue:
        nowx, nowy, cnt = queue.popleft()
        if maze[nowx][nowy] ==3:
            return cnt

        for x,y in [(0,1), (1,0), (0, -1), (-1,0)]:
            dx = nowx + x
            dy = nowy + y
            if 0<= dx <N and 0 <= dy <N:
                if not visitied[dx][dy] and maze[dx][dy] == 0:
                    visitied[dx][dy]= True
                    queue.append([dx,dy,cnt+1])
                elif not visitied[dx][dy] and maze[dx][dy] == 3:
                    visitied[dx][dy]= True
                    queue.append([dx,dy,cnt])
    return 0



T = int(input().rstrip())
for Tc in range(1,T+1):
    # N * N 배열
    N = int(input())
    maze= [list(map(int,input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] ==2:
                a, b = i, j
    start = (a,b)
    result =bfs(maze, start, N)
    print(f'#{Tc} {result}')
    