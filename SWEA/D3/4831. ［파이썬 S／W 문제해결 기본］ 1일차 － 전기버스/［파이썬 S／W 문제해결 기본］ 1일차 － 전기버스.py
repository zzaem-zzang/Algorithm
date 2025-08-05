'''
0번에서 출발해서 N번까지이동
K는 충전 후 최대거리
M개의 정류장
도착하지 못할경우 0
'''


T = int(input())

for Tc in range(T):
    K, N, M = map(int, input().split())
    M_lst = list(map(int, input().split()))
    pos = 0
    charge = 0

    while pos +K < N:
        for i in range(pos+K, pos, -1):
            if i in M_lst:
                pos = i
                charge +=1
                break

        else:
            charge = 0
            break

    print(f'#{Tc+1} {charge}')

