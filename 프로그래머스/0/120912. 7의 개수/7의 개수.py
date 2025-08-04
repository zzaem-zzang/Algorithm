def solution(array):
    answer = 0
    for ch in array:
        for char in str(ch):
            if char =='7':
                answer +=1
    return answer