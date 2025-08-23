N,M = map(int,input().split())
N_list = [list(map(int,input().split())) for _ in range(N)]
M_list = [list(map(int,input().split()))for _ in range(N)]
arr = [[0]* M for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr[i][j] = N_list[i][j] + M_list[i][j]


for i in range(N):
    for j in range(M):
        print(arr[i][j], end= ' ')
    print()