def recu(x,y,direction):
    global cnt
    if x == N-1 and y == N-1:
        cnt +=1
        return
    # 가로로 가는 경우
    if direction==1 or direction==3:
        if y+1 < N and pipe[x][y+1] == 0:
            recu(x,y+1,1)
    # 세로로 가는 경우
    if direction==2 or direction ==3:
        if x+1 < N and pipe[x+1][y] == 0:
            recu(x+1,y,2)
    
    if x+1 < N and y+1 < N:
        if pipe[x+1][y]==0 and pipe[x][y+1] == 0 and pipe[x+1][y+1]==0:
            recu(x+1,y+1,3)




N = int(input())
pipe = [list(map(int, input().split())) for _ in range(N)]
result = 0
pipe[0][0]=1 
pipe[0][1]=1
cnt = 0
direction = 1
recu(0,1,direction)
# dircetion 1 가로, 2 세로, 3 대각선
# initial dir = 1   [0][0]=1 [0][1]=1 
print(cnt)