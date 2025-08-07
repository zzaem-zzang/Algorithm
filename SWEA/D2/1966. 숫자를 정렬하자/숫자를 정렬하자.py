T = int(input())

for Tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]


    print(f'#{Tc+1} {" ".join(map(str,arr))}')

