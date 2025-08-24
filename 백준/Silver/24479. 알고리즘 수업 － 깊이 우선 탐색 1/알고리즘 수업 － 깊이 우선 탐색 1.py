import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(g,start, visited):
    global cnt
    visited[start] = cnt

    for i in graph[start]:  
        if visited[i] == 0:
            cnt +=1      
            dfs(graph, i, visited)

# N은 정점의 수 M은 간선의 수 R 시작 정점
N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] *(N+1)
for  _ in range(M):
    a , b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

cnt = 1
dfs(graph, R ,visited)
for i in range(1, N+1):
    print(visited[i])