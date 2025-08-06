T = int(input())
for Tc in range(1, T + 1):
    p, a_f, b_f = map(int, input().split())

    # A의 탐색
    a_start = 1
    a_end = p
    a_cnt = 0
    while True:
        a_mid = (a_start + a_end) // 2
        a_cnt += 1
        if a_mid == a_f:
            break
        elif a_mid > a_f:
            a_end = a_mid
        else:
            a_start = a_mid

    # B의 탐색
    b_start = 1
    b_end = p
    b_cnt = 0
    while True:
        b_mid = (b_start + b_end) // 2
        b_cnt += 1
        if b_mid == b_f:
            break
        elif b_mid > b_f:
            b_end = b_mid
        else:
            b_start = b_mid

    # 비교
    if a_cnt < b_cnt:
        print(f'#{Tc} A')
    elif a_cnt > b_cnt:
        print(f'#{Tc} B')
    else:
        print(f'#{Tc} 0')
