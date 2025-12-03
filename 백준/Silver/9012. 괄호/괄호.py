

T = int(input())


for _ in range(T):
    stack = []
    vps = input()
    flag = True
    for i in vps:
        if i =='(':
            stack.append('(')
        elif i ==')':
            if len(stack) ==0:
                flag= False
                break
            else:
                stack.pop()
    if len(stack)> 0:
        flag = False
    
    if flag == True:
        print('YES')
    else:
        print('NO')

    


