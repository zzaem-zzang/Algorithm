# 빨강 1 파랑2 보라3

T = int(input())

for Tc in range(T):

    result = 0
    I = int(input())
    arr = [[0] * 10 for i in range(10)]
    for _ in range(I):
        r1, r2 , c1, c2 , color = map(int,input().split())

        if color == 1:
            for i in range(r1, c1+1):
                for j in range(r2, c2+1):
                     if arr[i][j] == 2:
                         arr[i][j] = 3
                     elif arr[i][j] == 0:
                         arr[i][j] = 1

        elif color ==2:
            for i in range(r1, c1+1):
                for j in range(r2, c2+1):
                    if arr[i][j] == 1:
                        arr[i][j] =3
                    elif arr[i][j] == 0:
                        arr[i][j] =2


    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 3:
                result +=1


    print(f'#{Tc+1} {result}')