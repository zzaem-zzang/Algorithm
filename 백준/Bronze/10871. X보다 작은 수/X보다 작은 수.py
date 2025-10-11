N, X = map(int,input().split())
lst = list(map(int,input().split()))
for n in range(N):
    if lst[n]< X :
        print(lst[n], end=' ')
    else:
        continue