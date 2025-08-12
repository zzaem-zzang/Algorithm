
N = int(input())
arr = list(map(int,input().split()))

lst = []

for i in range(N):
    lst.insert(i-arr[i], i+1)

print(*lst)