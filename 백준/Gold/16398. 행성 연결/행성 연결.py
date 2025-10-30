import heapq

def prim():
    visited = [False] * (N+1)
    q = [(0, 1)]  # (비용, 시작노드)
    total = 0

    while q:
        cost, node = heapq.heappop(q)
        if visited[node]:
            continue
        visited[node] = True
        total += cost

        for nxt_cost, nxt in planet[node]:
            if not visited[nxt]:
                heapq.heappush(q, (nxt_cost, nxt))
    
    print(total)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

planet = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(i+1, N):
        planet[i+1].append((lst[i][j], j+1))
        planet[j+1].append((lst[i][j], i+1))

prim()
