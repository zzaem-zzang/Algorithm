n = int(input())

dp = [0] *(n+1)


for i in range(1, n+1):
    dp[i] = i # 모두 1로 생성하면 최대 i개
    j = 1
    while j **2 <= i:
        dp[i] = min(dp[i], dp[i -j**2] + 1)
        j += 1
print(dp[n])