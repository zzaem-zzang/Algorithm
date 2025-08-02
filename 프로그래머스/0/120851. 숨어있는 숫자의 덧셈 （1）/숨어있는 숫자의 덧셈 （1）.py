def solution(my_string):
    answer = 0
    my_stirng = list(my_string)
    
    for ch in my_string:
        if ch.isdigit():
            answer += int(ch)
    return answer