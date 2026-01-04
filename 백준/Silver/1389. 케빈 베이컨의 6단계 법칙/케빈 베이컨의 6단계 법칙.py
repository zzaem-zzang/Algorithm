# N은 유저의 수 , M은 친구 관계의 수

from collections import deque


N, M = map(int, input().split())


# 친구 관계를 저장할 그래프
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    a , b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def func(start):
    cnt = 0
    
    for others in range(1, N + 1):
        visited = [False] * (N+1)
        if start != others:
            queue = deque()
            queue.append((start, 0))
            visited[start] = True
            while queue:
                pos, depth = queue.popleft()
                if pos == others:
                    cnt += depth
                    break

                for next_pos in graph[pos]:
                    if not visited[next_pos]:
                        visited[next_pos]= True
                        queue.append((next_pos, depth + 1))
        
    return cnt

num = -1
val = float('inf')

for i in range(1, N + 1):
    find = func(i)
    if find < val:
        val = find
        num = i

print(num)



