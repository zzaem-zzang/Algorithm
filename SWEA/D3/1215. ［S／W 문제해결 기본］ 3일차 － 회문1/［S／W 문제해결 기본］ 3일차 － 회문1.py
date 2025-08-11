
for T in range(1,11):
    char = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(input()))
    cnt = 0
    for i in range(8):
        flag = False
        for j in range(len(arr)-char+1):
            for k in range(char//2):
                if arr[i][j+k] != arr[i][j+char-k-1]:
                    flag= False
                    break
                else:
                    flag= True
                
            if flag:
                cnt +=1
    
    for i in range(len(arr)-char+1):
        flag = False
        for j in range(8):
            for k in range(char//2):
                if arr[i+k][j] != arr[i+char-k-1][j]:
                    flag= False
                    break
                else:
                    flag= True
                
            if flag:
                cnt +=1

    print(f'#{T} {cnt}')