def solution(n):
    all_total = 0
    
    for i in range(1,n+1):
        total = 0
        for j in range(1,i+1):
            if i % j ==0:
                total +=1
                if total >= 3:
                    all_total+=1
                    break
    return all_total