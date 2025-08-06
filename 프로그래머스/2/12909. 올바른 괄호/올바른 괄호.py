# 스택 활용

def solution(s):
    stack = []
    result =True
    for char in s:
        if char =='(':
            stack.append(char)
        elif char ==')':
            if not stack:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        result = True
    elif len(stack) > 0:
        result = False
    return result