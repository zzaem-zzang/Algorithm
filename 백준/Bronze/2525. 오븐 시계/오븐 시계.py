H, M = map(int, input().split())
minute = int(input())

M += minute
H += M//60
M = M% 60
H = H % 24

print(H, M)

