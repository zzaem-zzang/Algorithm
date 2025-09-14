# n이 카드갯수 k가 몇장
def dfs(cnt,card=''):
    if cnt ==k:
        combi.add(card)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            dfs(cnt+1,card+cards[i])
            visited[i]=False




n = int(input())
k = int(input())
cards= []
combi=set()
for _ in range(n):
    c = input()
    cards.append(c)
visited = [False] * n
dfs(0,'')
print(len(combi))