def solution(n):
    start = 1
    total = 1
    while n >= total:
        start +=1
        total = total * start
        
    start = start-1
    return start
    