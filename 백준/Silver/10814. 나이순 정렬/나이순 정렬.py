import sys
input = sys.stdin.readline

N = int(input())

lst = []

for i in range(N):
    a , b = input().split()
    lst.append([int(a), i, b])

lst.sort(key= lambda x : (x[0], x[1]))

for a in range(N):
    print(f'{lst[a][0]} {lst[a][2]}')