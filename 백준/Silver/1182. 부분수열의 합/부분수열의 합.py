def subset_sum(idx,sub_sum):
    global cnt

    if idx >= N:
        return

    sub_sum += arr[idx]

    if sub_sum == S:
        cnt +=1

    subset_sum(idx+1,sub_sum)
    subset_sum(idx+1, sub_sum-arr[idx])


N, S = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
subset_sum(0,0)
print(cnt)