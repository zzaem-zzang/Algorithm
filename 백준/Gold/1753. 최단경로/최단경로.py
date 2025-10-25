import heapq
import sys
input = sys.stdin.readline

def Dijkstra(start):
    distance[start] = 0 
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)

    while q:
        dista, now = heapq.heappop(q)
        if distance[now] < dista:  # 이미 처리된 노드면 스킵
            continue
        for nxt_node, cost in graph[now]:
            if distance[nxt_node] > dista + cost:
                distance[nxt_node] = dista + cost
                heapq.heappush(q, (distance[nxt_node], nxt_node))

INF = int(1e9)
V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

Dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
