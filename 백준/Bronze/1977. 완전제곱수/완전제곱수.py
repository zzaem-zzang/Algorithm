arr =[]
M = int(input())
N = int(input())

for i in range(M,N+1):
    root_i = i**(0.5)
    if root_i.is_integer():
        arr.append(i)
    
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)