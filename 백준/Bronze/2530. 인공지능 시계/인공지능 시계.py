H, M, S = map(int, input().split())
second = int(input())

S += second
M += S //60
S %= 60
H += M //60
M %= 60
H %= 24


print(H, M, S)

