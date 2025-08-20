# 문제에서 원하는 것은 마지막까지 남아있는 피자번호 !
import collections


def pizza(N,M,arr):
    oven = collections.deque() #오븐에 있는 피자
    pizza_list= collections.deque() 

    for i in range(M):
        pizza_list.append([i+1, arr[i]]) # 피자에 대한 인덱싱
    
    for _ in range(N):
        oven.append(pizza_list.popleft()) # 화덕에 들어갈 수 있는 최대 피자
    
    last_pizza = 0
    while len(oven) > 1:
        num , cheese = oven.popleft()
        cheese //=2
        if cheese == 0:
            last_pizza = num
            if pizza_list:
                oven.append(pizza_list.popleft())
        else:
            oven.append([num, cheese])
    return oven[0][0]    
    

T = int(input())
for Tc in range(1, T+1):
    # N은 화덕의 크기 M은 피자 개수
    # Ci는 뿌려진 치즈의 양
    N, M = map(int, input().split())
    Ci = list(map(int,input().split()))
    result = pizza(N, M, Ci)
    print(f'#{Tc} {result}')