# 정상적으로 짝을 이룬 경우 1 , 아닌 경우 0
# T = test case

T = int(input())
for Tc in range(1,T+1):
    chr = input()
    stack = []
    flag =1

    sub_set = {')':'(', '}':'{'}
    for ch in chr:
        if ch in '({':
            stack.append(ch)
            
        elif ch in ')}':
            if not stack:
                flag = 0
                break
            elif stack[-1] == sub_set[ch]:
                stack.pop()
            else:
                flag= 0
                break
    if stack:
        flag = 0 
    print(f'#{Tc} {flag}')

