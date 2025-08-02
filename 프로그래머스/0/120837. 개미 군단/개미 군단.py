def solution(hp):
    answer = 0 # 병력 수
    
    while hp!=0:
        if hp >=5:
            answer +=1
            hp -=5
        elif hp >=3:
            answer +=1
            hp -=3
        elif hp >=1:
            answer +=1
            hp -=1
    return answer
        
    
    
    
    return answer