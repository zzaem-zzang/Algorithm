def solution(my_string):
    my_string = my_string.lower()
    answer = sorted(my_string)
    
    return ''.join(answer)