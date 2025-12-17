N = int(input())

lst = list(map(int, input().split()))

dp = [0] * (N)
prev = [-1] * N
dp[0] = 1

for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

print(max(dp))

idx = dp.index(max(dp))
result = []
while idx != -1:
    result.append(lst[idx])
    idx = prev[idx]

result.reverse()
print(' '.join(map(str, result)))
            

