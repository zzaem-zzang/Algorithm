
def dfs(cnt,a,b):
    global min_val
    if cnt == N:
        if a==1 and b==0:
            return
        min_val = min(min_val, abs(a-b))
        return

    dfs(cnt+1,a * S[cnt], b +B[cnt])
    dfs(cnt+1,a , b )



N = int(input())
# 신맛S 쓴맛 B
S = []
B = []
for _ in range(N):
    s,b  = map(int,input().split())
    S.append(s)
    B.append(b)
min_val = 1000000000
dfs(0,1,0)
print(min_val)
