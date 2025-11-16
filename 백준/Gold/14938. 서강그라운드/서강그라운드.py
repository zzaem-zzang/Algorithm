# 지역의 개수 n , 예은이의 수색 범위 m, 길의 개수 r
INF = int(1e9)
n, m, r = map(int,input().split())
cost = list(map(int, input().split()))
graph = [[INF] *(n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
result = 0
for i in range(1,n+1):
    total = 0
    for j in range(1,n+1):
        if graph[i][j] <= m:
            total += cost[j-1]
    if total> result:
        result = total        

print(result)
                  
