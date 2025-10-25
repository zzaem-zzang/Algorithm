
def dfs(cnt, ans=[]):
    if len(ans) == M:
        print(*ans)
        return
    
    for i in range(cnt,N):
        cnt += 1
        ans.append(lst[i])
        dfs(cnt, ans)
        ans.pop()
        

N, M = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()


dfs(0, [])