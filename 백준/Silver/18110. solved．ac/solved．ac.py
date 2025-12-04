import sys
from math import ceil, floor
input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
    exit()

lst = [int(input()) for _ in range(N)]
lst.sort()

m = 0.15 * N
if m - int(m) >= 0.5:
    m = ceil(m)
else:
    m = floor(m)

down = m
up = N - m

ans = lst[down:up]

avg = sum(ans) / len(ans)
print(int(avg + 0.5))  
