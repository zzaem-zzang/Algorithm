N, M = map(int,input().split())
lst = N * [0]
for _ in range(M):
    i, j, k = map(int,input().split())
    for a in range(i,j+1):
        lst[a-1]= k
print(*lst)