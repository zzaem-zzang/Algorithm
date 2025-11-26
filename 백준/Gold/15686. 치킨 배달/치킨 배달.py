from itertools import combinations

N, M = map(int, input().split())
ways = []

home = []
chicken = []

for _ in range(N):
    way = list(map(int, input().split()))
    ways.append(way)

for i in range(N):
    for j in range(N):
        if ways[i][j] == 1:
            home.append((i, j))
        elif ways[i][j] == 2:
            chicken.append((i,j))

INF = 1e9
answer = INF

for selected in combinations(chicken, M):
    cost = 0    # 현재 선택된 치킨집에서의 최소 비용
    for x, y in home:
        min_temp = INF
        for xx, yy in selected:
            temp = abs(x-xx) + abs(y-yy)
            min_temp = min(min_temp, temp)
        cost+= min_temp
    answer= min(cost, answer)
print(answer)