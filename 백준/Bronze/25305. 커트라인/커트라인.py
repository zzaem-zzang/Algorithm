T , reward = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
res = arr[reward-1]
print(res)