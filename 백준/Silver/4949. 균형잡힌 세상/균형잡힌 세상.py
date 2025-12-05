



while True:
    string = input()
    if string[0] =='.':
        break
    else:
        flag = True
        stack = []
        for s in string:
            if s=='(' or s=='[':
                stack.append(s)
            elif s==')' or s== ']':
                if len(stack) > 0 :
                    p = stack.pop()
                    if p == '(' and s ==')':
                        continue
                    elif p =='[' and s ==']':
                        continue
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
        if len(stack)>0:
            flag = False

        if flag:
            print('yes')
        else:
            print('no')