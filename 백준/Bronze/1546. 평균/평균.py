M = int(input())
arr = list(map(int,input().split()))
MV = max(arr)
arr2 = []
for a in arr:
    arr2.append(a/MV*100)
print(sum(arr2)/len(arr2))