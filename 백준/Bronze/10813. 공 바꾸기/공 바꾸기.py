N, M = map(int, input().split())
lst = [i+1 for i in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    lst[a-1], lst[b-1]= lst[b-1],lst[a-1]
print(*lst)