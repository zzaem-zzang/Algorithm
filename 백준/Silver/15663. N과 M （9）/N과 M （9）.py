# N개의 자연수와 자연수 M
# 길이가 M인 수열

def dfs(size):
    if size == M:
        # 길이가 M이면 출력
        print(*new_arr)
        return
    # 중복수열을 막기 위해 use 사용
    use = -1
    for i in range(N):
        if not visited[i] and use != arr[i]:
            visited[i] = True
            new_arr.append(arr[i])
            use = arr[i]
            dfs(size+1)
            visited[i]=False
            new_arr.pop()


N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
visited =[False]* N
new_arr = []
dfs(0)

