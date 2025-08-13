# 과자한개가격 K 과자개수 N 현재 돈 M
K, N, M = map(int, input().split())
if K * N > M:
    print(K*N-M)
else:
    print(0)