from collections import deque

def cipher_making(cipher):
    # deque 만들기
    cipher = deque(cipher)
    increase = [1,2,3,4,5]
    seq = 0
    while True:
        temp = cipher.popleft()
        temp -= increase[seq]
        seq = (seq+1)%5
        if temp <= 0 :
            cipher.append(0)
            break
        cipher.append(temp)
    
    return cipher
        

T = 10
# 8개의 숫자를 입력 .. 1번쨰 1감소 맨뒤 -> 2번쨰 2감소 맨뒤 -> 3번째 3감소 맨뒤
for Tc in range(1, T+1):
    input()
    # 암호 8 글자 생성
    cipher = list(map(int,input().split()))
    result = cipher_making(cipher)
    print(f'#{Tc} {" ".join(map(str,result))}')


