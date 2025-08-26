def dfs(start):
    global cnt
    stack = [start]
    visited[start] = True

    while stack:
        item = stack.pop()
        for i in graph[item]:
            if not visited[i]:
                visited[i] = True
                cnt +=1
                stack.append(i)

node = int(input())
line = int(input())
visited = [False] * (node+1)
graph = [[] for _ in range(node+1)]
for _ in range(line):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
dfs(1)
print(cnt)