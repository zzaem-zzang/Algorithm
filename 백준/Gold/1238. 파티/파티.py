import heapq

def answer(i):
    h = []
    heapq.heappush(h,(0, i))
    cost = [float('inf')] *(N+1)
    cost[i] = 0
    while h:
        now_cost, now_pos = heapq.heappop(h)
        if now_cost > cost[now_pos]:
            continue

        for nxt_cost, nxt_pos in graph[now_pos]:
            total_cost = now_cost + nxt_cost
            if total_cost < cost[nxt_pos]:
                cost[nxt_pos] = total_cost
                heapq.heappush(h,(total_cost,nxt_pos))
    return cost

N, M, X = map(int , input().split())

graph= [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c =map(int,input().split())
    graph[a].append((c,b))


result = 0
for i in range(1,N+1):
    go = answer(i)
    back = answer(X)
    result = max(go[X]+back[i], result)

print(result)


