def row(x):
    global cnt
    used = [False] * N
    for i in range(N - 1):
        if abs(way[x][i] - way[x][i + 1]) > 1:
            break

        # 내리막인 경우
        if way[x][i] == way[x][i + 1] + 1:
            for j in range(L):
                if (i + 1 + j) >= N or way[x][i + 1] != way[x][i + 1 + j] or used[i + 1 + j]:
                    break
            else:
                for j in range(L):
                    used[i + 1 + j] = True
                continue
            break

        # 오르막인 경우
        elif way[x][i] == way[x][i + 1] - 1:
            for j in range(L):
                if (i - j) < 0 or way[x][i] != way[x][i - j] or used[i - j]:
                    break
            else:
                for j in range(L):
                    used[i - j] = True
                continue
            break

        elif way[x][i] == way[x][i + 1]:
            continue
        else:
            break
    else:
        cnt += 1


def col(x):
    global cnt
    used = [False] * N
    for i in range(N - 1):
        if abs(way[i][x] - way[i + 1][x]) > 1:
            break

        # 내리막인 경우
        if way[i][x] == way[i + 1][x] + 1:
            for j in range(L):
                if (i + 1 + j) >= N or way[i + 1][x] != way[i + 1 + j][x] or used[i + 1 + j]:
                    break
            else:
                for j in range(L):
                    used[i + 1 + j] = True
                continue
            break

        # 오르막인 경우
        elif way[i][x] == way[i + 1][x] - 1:
            for j in range(L):
                if (i - j) < 0 or way[i][x] != way[i - j][x] or used[i - j]:
                    break
            else:
                for j in range(L):
                    used[i - j] = True
                continue
            break

        elif way[i][x] == way[i + 1][x]:
            continue
        else:
            break
    else:
        cnt += 1


N, L = map(int, input().split())
way = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    row(i)
    col(i)

print(cnt)
