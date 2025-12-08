N, M = map(int ,input().split())
dict = {}

for _ in range(N):
    A, B = input().split()
    dict[A] = B

for _ in range(M):
    m = input()
    print(dict[m])