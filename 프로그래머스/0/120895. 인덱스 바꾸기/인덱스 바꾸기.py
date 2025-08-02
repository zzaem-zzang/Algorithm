def solution(my_string, num1, num2):
    ch = list(my_string)
    ch[num1], ch[num2] = ch[num2], ch[num1]
    
    return ''.join(ch)