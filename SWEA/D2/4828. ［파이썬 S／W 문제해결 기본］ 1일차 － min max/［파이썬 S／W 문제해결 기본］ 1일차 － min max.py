T = int(input())
 
for Tc in range(T):
    N = input()
    arr = list(map(int, input().split()))
    max_val = arr[0]
    min_val = arr[0]
 
    for i in range(len(arr)):
        if max_val < arr[i]:
            max_val = arr[i]
 
    for i in range(len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
 
    result = max_val - min_val
    print(f'#{Tc+1} {result}')