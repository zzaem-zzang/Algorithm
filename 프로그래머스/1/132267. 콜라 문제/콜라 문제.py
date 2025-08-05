def solution(a, b, n):
    answer = 0
    while n >= a:
        newCount = n // a * b
        leftover = n % a
        
        answer += newCount
        n = leftover + newCount
    return answer
