T = int(input())
 
for Tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    first_sum = sum(arr[:M])
    max_val = first_sum
    min_val = first_sum
 
 
    for i in range(0,N-M+1):
        total_max = 0
        for j in range(i, i+M):
            total_max += arr[j]
        if max_val < total_max:
            max_val = total_max
 
    for i in range(0, N-M+1):
        total_min = 0
        for j in range(i, i + M):
            total_min += arr[j]
        if min_val > total_min:
            min_val = total_min
 
    diff = max_val-min_val
    print(f'#{Tc+1} {diff}')