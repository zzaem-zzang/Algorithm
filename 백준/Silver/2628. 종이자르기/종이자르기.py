def check_arr(cond, r, row, col, cuts_row, cuts_col):
    if cond == 0:  # 가로로 자르기
        cnt1 = r      # 위쪽 영역 높이
        cnt2 = row-r  # 아래쪽 영역 높이
        if cnt1 >= cnt2:
            cuts_row.append(r)   # 위쪽 선택
        else:
            cuts_row.append(r)   # 아래쪽 선택 (결국 동일 → 위치만 기록)
    elif cond == 1:  # 세로로 자르기
        cnt1 = r      # 왼쪽 영역 폭
        cnt2 = col-r  # 오른쪽 영역 폭
        if cnt1 >= cnt2:
            cuts_col.append(r)   # 왼쪽 선택
        else:
            cuts_col.append(r)   # 오른쪽 선택 (역시 동일)

col, row = map(int, input().split())
num = int(input())

cuts_row = [0, row]  # 세로 자른 위치
cuts_col = [0, col]  # 가로 자른 위치

for _ in range(num):
    cond, r = map(int, input().split())
    check_arr(cond, r, row, col, cuts_row, cuts_col)

# 정렬 후 가장 큰 차이 구하기
cuts_row.sort()
cuts_col.sort()

max_h = max(cuts_row[i+1] - cuts_row[i] for i in range(len(cuts_row)-1))
max_w = max(cuts_col[i+1] - cuts_col[i] for i in range(len(cuts_col)-1))

print(max_h * max_w)
