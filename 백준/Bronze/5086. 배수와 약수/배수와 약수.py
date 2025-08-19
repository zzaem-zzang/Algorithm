while True:
    N, M = map(int, input().split())
    
    # 종료 조건
    if N == 0 and M == 0:
        break
    
    if N % M == 0:
        print('multiple')
    elif M % N == 0:
        print('factor')
    else:
        print('neither')
