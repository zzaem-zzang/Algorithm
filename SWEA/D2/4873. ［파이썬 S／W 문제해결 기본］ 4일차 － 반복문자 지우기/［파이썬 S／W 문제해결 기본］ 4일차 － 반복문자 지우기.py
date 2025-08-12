T = int(input())
# 문자열 s에서 반복된 문자 삭제
for Tc in range(1,T+1):
    stack = []
    char = input()

    for s in char:
        stack.append(s)
        if len(stack) >1 and stack[-2] == stack[-1]:
            stack =stack[:-2]

    result = 0
    for _ in range(len(stack)):
        result +=1
    print(f'#{Tc} {result}')    
        

            