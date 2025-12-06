from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int,input().split()))
    
    queue = deque()
    
    for i, v in enumerate(lst):
        queue.append((v,i)) # v는 값 // i 는 중요도  i가 클수록 중요도 높음

    cnt = 0
    

    while True:
        now = queue.popleft()
        max_value = -1

        for item in queue:
            if item[0] > max_value:
                max_value = item[0]

        if now[0] < max_value:
            queue.append(now)
        else:
            cnt += 1
            if now[1] == M:
                print(cnt)
                break