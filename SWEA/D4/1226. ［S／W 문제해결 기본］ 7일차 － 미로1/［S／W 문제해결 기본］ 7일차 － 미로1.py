from collections import deque
# 1 가능함 0 가능하지 않음 -> 알고자 하는 값
# 0:길 , 1:벽, 2:출발점, 3:도착점

def bfs(maze,start, stop):
    queue = deque()
    a,b = start
    queue.append((a,b))
    visited =[[False]* 16 for _ in range(16)]
    visited[a][b]= True

    while queue:
        now_x, now_y = queue.popleft()
        if maze[now_x][now_y]==3:
            return 1
        for x, y  in [(0,1), (0, -1), (1,0), (-1,0)]:
            dx = now_x +x
            dy = now_y +y
            if 0<= dx < 16 and 0<= dy < 16:
                if not visited[dx][dy] and (maze[dx][dy] ==0 or maze[dx][dy]==3):
                    queue.append((dx,dy))
                    visited[dx][dy]= True
    return 0



T = 10
for Tc in range(1, T+1):
    t= input()
    maze =  [list(map(int, input().strip())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            elif maze[i][j] == 3:
                stop_x, stop_y = i,j
    start = start_x, start_y
    stop = stop_x, stop_y
    result = bfs(maze, start, stop)
    print(f'#{Tc} {result}')
    
