N, M = map(int, input().split())
lst = [i for i in range(1,N+1)]
for m in range(M):
    a, b = map(int, input().split())
    lst[a-1:b] = lst[a-1:b][::-1]
print(*lst)