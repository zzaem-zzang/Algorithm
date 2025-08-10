T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0

    for i in range(N):
        for j in range(N):
            total = sum(arr[i]) + sum(row[j] for row in arr) - arr[i][j]
            if max_val < total:
                max_val = total
    
    print(f"#{Tc} {max_val}")
