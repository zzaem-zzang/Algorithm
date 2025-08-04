T = int(input())
 
for Tc in range(T):
    N, K = map(int,input().split()) # N 배열길이 K문자길이
    arr = [list(map(int,input().split())) for _ in range(N)]
    total = 0
 
 
    for i in range(N):
        cnt = 0
        # 가로 갯수 확인
        for j in range(N):
            if arr[i][j] == 1:
                cnt +=1
            # 연결이 끝이거나 , 0 을 만날경우 초기화
            if arr[i][j] ==0 or j == N-1:
                if  cnt == K:
                    total +=1
                cnt = 0 
        # 세로 갯수 확인
        for j in range(N):
            if arr[j][i] == 1:
                cnt +=1
             
            if arr[j][i] == 0 or j == N-1:
                if cnt == K:
                    total +=1
                cnt = 0
 
    print(f'#{Tc+1} {total}')