# 7명의 여학생 구성
# 7명의 자리는 서로 가로나 세로로 반드시 인접
# 이다솜의 학생들로구만 구성 X
# 이다솜파가 우위 -> 4명이상 
# S는 이다솜파 Y는 임도연파
from collections import deque

def bfs(si,sj):
    q = deque()
    vv = [[0]*5 for _ in range(5)]    
    q.append((si,sj))
    vv[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5:
                if v[ni][nj] == 1 and vv[ni][nj] == 0:
                    vv[ni][nj] = 1
                    q.append((ni,nj))
                    cnt += 1
    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i, j)
                

def dfs(n, cnt, scnt):
    global ans

    if cnt>7:
        return
    
    if n == 25:
        if cnt == 7 and scnt >= 4:
            # 인접했을지 체크해서 + 1
            if check():
                ans += 1
        return
    # 포함하는 경우    
    v[n//5][n%5] = 1
    dfs(n+1, cnt+1, scnt + int(arr[n//5][n%5] == 'S'))
    # 원상복구
    v[n//5][n%5] = 0
    # 포함하지 않는 경우
    dfs(n+1, cnt, scnt) 


arr = [input() for _ in range(5)]
ans = 0
v = [[0]*5 for _ in range(5)]
# 인덱스번호(0,24), 포함학생수 , 다솜학생수
dfs(0,0,0)
print(ans)