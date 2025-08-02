def solution(box, n):
    answer = 1
    for size in box:
        answer *= size // n
    return answer
