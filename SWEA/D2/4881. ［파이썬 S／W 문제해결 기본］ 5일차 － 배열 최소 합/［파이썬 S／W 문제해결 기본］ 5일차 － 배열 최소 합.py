# 백트래킹의 핵심은 가지치기
def dfs(i,total):
    global min_sum
    if total >= min_sum:
        return
    
    if i == N:
        min_sum= min(min_sum,total)
        return
    
    for j in range(N):
        if not visited[j]: #선택되지 않은 열이라면
            visited[j]= True
            dfs(i+1, total+arr[i][j])
            visited[j]= False


T = int(input())
for Tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_sum = float('inf')

    dfs(0,0)
    print(f'#{Tc} {min_sum}')