T = int(input())

for Tc in range(1,T+1):
    arr = [0] *5001
    result = []
    N = int(input())
    for _ in range(N):
        a, b = map(int,(input().split()))
        for i in range (a,b+1):
            arr[i] += 1
    P = int(input())
    stops = [int(input()) for _ in range(P)]
    result = [str(arr[stop]) for stop in stops]
    print(f'#{Tc} {" ".join(result)}')