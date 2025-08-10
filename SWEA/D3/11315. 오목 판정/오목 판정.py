T = int(input())

for Tc in range(T):
    N = int(input())
    flag = 'NO'
    arr = [list(input()) for _ in range(N)]
    # 오목판 생성 완료
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i][j] =='o':
                cnt +=1
                if cnt == 5:
                    flag ='YES'
                    break
            else:
                cnt = 0

    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[j][i] =='o':
                cnt +=1
                if cnt == 5:
                    flag ='YES'
                    break
            else: 
                cnt = 0

    for i in range(0,len(arr)-4):
        for j in range(0,len(arr)-4):
            cnt = 0
            for k in range(0,5): 
                if arr[i+k][j+k] =='o':
                    cnt +=1
                    if cnt == 5:
                        flag ='YES'
                        break
                else:
                    cnt = 0
                    
    
    for i in range(0,len(arr)-4):
        for j in range(4,len(arr)):
            cnt = 0
            for k in range(0,5): 
                if arr[i+k][j-k] =='o':
                    cnt +=1
                    if cnt == 5:
                        flag ='YES'
                        break
                else:
                    cnt = 0
                    
    print(f'#{Tc+1} {flag}')
