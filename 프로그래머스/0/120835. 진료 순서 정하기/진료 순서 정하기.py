def solution(emergency):
    answer = []
    emer = sorted(emergency, reverse= True)
    
    for i in emergency:
        answer.append(emer.index(i)+1)
    
    return answer