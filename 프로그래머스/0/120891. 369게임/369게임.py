def solution(order):
    cnt = 0 
    for ch in str(order):
        if ch =='3' or ch =='6' or ch =='9':
            cnt +=1
    
    return cnt