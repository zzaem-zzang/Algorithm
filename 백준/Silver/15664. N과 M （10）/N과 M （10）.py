
def dfs(cnt):
    if len(result) == M:
        print(*result)
        return
    
    check = 0
    for i in range(cnt,N):
        if lst[i] !=  check:
            check = lst[i]
            result.append(lst[i])
            dfs(i+1)
            result.pop()
        
        
N, M = map(int, input().split())
lst = list(map(int,input().split()))
result = []
lst.sort()
dfs(0)
