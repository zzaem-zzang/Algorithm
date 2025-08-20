# DFS와 BFS탐색
# 방문할 수 있는 점이 여러개 일 경우 작은 번호 먼저 방문
# N은 정점의 개수, M은 간선의 개수 , 시작 정점 V
# BFS를 위해서 dequeue import
from collections import deque

def dfs(start_node):
    print(start_node, end=' ')
    d_visitied[start_node] = True
    for i in graph[start_node]:
        if not d_visitied[i]:
            dfs(i)
# i-1 현 위치 조사
# i-2 현재에서 갈 수 있는 위치
# i-3 이동한 자리에서 갈 수 있는 위치
def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    b_visitied[start_node] = True

    while queue:
        move = queue.popleft()
        print(move, end=' ')
        for i in graph[move]:
            if not b_visitied[i]:
                queue.append(i)
                b_visitied[i] = True

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    line1, line2 = map(int, input().split())
    graph[line1].append(line2)
    graph[line2].append(line1)
for g in graph:
    # 낮은 번호부터 이동
    g.sort()
d_visitied =[False] *(N+1)
b_visitied =[False] *(N+1)
dfs(V)
print()
bfs(V)