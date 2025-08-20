from collections import deque as dq

def deck_circulator(arr, M):
    # deque로 변환
    # i-1
    arr= dq(arr)
    for _ in range(M):
        temp = arr.popleft()
        arr.append(temp)
    return arr[0]
    
    # i-2
    # arr = dq(arr)
    # arr.rotate(-M)
    # return arr[0]


T = int(input())
for Tc in range(1,T+1):
    # N은 배열길이 M은 횟수
    N , M = map(int, input().split())
    arr = list(map(int,input().split()))
    result = deck_circulator(arr, M)
    print(f'#{Tc} {result}')