N, M = map(int,input().split())
board = [input() for _ in range(N)]
result = float('inf')

for i in range(N-7):
    for j in range(M-7):
        wh = 0
        bl = 0
        for I in range(i,i+8):
            for J in range(j,j+8):
                if (I+J) % 2 ==0 :
                    if board[I][J] != 'W':
                        wh +=1
                    if board[I][J] != 'B':
                        bl +=1
                else:
                    if board[I][J] != 'B':
                        wh +=1
                    if board[I][J] != 'W':
                        bl +=1
        result = min(wh,bl,result)
print(result)

