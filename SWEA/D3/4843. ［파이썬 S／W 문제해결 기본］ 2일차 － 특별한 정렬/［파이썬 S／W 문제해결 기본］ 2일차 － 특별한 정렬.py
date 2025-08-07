T = int(input())

for Tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0,len(arr)-1):
        max_idx = i
        min_idx = i

        if i% 2 ==0:
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[max_idx], arr[i] = arr[i], arr[max_idx]

        elif i % 2 == 1:
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

    print(f'#{Tc+1} {" ".join(map(str,arr[:10]))}')

