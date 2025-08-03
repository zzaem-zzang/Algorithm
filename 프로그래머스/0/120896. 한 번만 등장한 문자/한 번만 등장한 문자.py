def solution(s):
    answer = []
    s = list(s)
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            answer.append(s[i])
    answer.sort()
    answer =''.join(answer)
    return answer