board = []
say = []
say_count = []
cnt = 0

# 빙고판 입력
for _ in range(5):
    board.append(list(map(int, input().split())))

# 부르는 번호 입력
for _ in range(5):
    say.append(list(map(int, input().split())))

found = False  

for i in range(5):
    for j in range(5):
        say_count.append(say[i][j])
        cnt += 1
        bingo = 0  

        # 가로 체크
        for x in range(5):
            if all(board[x][y] in say_count for y in range(5)):
                bingo += 1

        # 세로 체크
        for y in range(5):
            if all(board[x][y] in say_count for x in range(5)):
                bingo += 1

        # 대각선 체크
        if all(board[x][x] in say_count for x in range(5)):
            bingo += 1
        if all(board[x][4-x] in say_count for x in range(5)):
            bingo += 1

        if bingo >= 3:
            print(cnt)
            found = True  # 루프 종료 표시
            break  # j 루프 탈출
    if found:
        break  # i 루프 탈출
