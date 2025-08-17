col, row = map(int, input().split())
num = int(input())

cuts_row = [0, row]  # 가로 방향 컷 (세로 좌표)
cuts_col = [0, col]  # 세로 방향 컷 (가로 좌표)

for _ in range(num):
    cond, r = map(int, input().split())
    if cond == 0:
        cuts_row.append(r)  # 가로 자르기 → 세로 길이 분할
    else:
        cuts_col.append(r)  # 세로 자르기 → 가로 길이 분할

# 정렬
cuts_row.sort()
cuts_col.sort()

# 가장 큰 차이 구하기
max_h = max(cuts_row[i+1] - cuts_row[i] for i in range(len(cuts_row)-1))
max_w = max(cuts_col[i+1] - cuts_col[i] for i in range(len(cuts_col)-1))

print(max_h * max_w)
