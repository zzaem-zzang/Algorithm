T = int(input())

for Tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    result = [0]* N

    for n in range(N):
        cnt =  0
        for col in range(n+1, N):
            if arr[n] > arr[col]:
                cnt +=1
        result[n] = cnt
    max_gravity = 0

    for num in range(len(result)):
        if result[num]> max_gravity:
            max_gravity = result[num]
    
    print(f'#{Tc+1} {max_gravity}')