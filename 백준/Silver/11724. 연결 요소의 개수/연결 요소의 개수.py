import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def find(x):
    visited[x] = True
    stack = [x]
    
    while stack:
        s = stack.pop()
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)    

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        find(i)
        cnt += 1

print(cnt)



