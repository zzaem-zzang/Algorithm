def solution(s):
    s = s.split(' ')
    m = float('inf')
    M = float('-inf')

    for i in range(len(s)):
        if  int(s[i]) < m :
            m = int(s[i])
        if int(s[i]) > M :
            M =int(s[i])
        
    return f"{m} {M}"