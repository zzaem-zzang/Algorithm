def solution(my_string):
    answer = []
    
    for ch in my_string:
        if ch not in answer:
            answer.append(ch)
        
    return ''.join(answer)