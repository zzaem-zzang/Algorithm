def solution(array, n):
    m = abs(array[0]-n)
    val = array[0]
    
    for a in array:
        near = abs(a-n)
        if near < m:
            val = a
            m = near
        elif near == m:
            val = min(val, a)
    
    return val