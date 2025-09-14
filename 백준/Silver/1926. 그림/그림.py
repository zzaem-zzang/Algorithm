from collections import deque




def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    board[x][y] = 0
    area = 1

    while dq:
        a, b = dq.popleft()
        for A,B in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = a+A, b+B
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
                board[nx][ny]=0
                dq.append((nx,ny))
                area+=1
    return area



n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
max_val =0
cnt =0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt+=1
            result =bfs(i,j)
            max_val=max(result,max_val)

print(cnt)
print(max_val)
