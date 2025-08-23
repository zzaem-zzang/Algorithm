N, M = input().split()
arr =list(map(int,input().split()))
leng = len(arr)
max_val = -1
for i in range(leng):
    for j in range(i+1,leng):
        for k in range(j+1,leng):
            val = arr[i]+arr[j]+arr[k]
            if int(M)>=val > max_val:
                max_val = val
print(max_val)