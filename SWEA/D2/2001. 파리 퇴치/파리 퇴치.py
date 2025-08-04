T = int(input())
 
for Tc in range(T):
    N , M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_val =0
     
    for i in range(0,N-M+1):
        for j in range(0,N-M+1):
            total = 0
            for a in range(i,i+M):
                for b in range(j,j+M):
                    total+=arr[a][b]
            if total > max_val:
                max_val = total
    print(f'#{Tc+1} {max_val}')