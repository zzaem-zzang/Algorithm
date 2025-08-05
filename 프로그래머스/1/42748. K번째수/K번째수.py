def solution(array, commands):
    answer = []
    for i,j,k in commands:
        arr =array[i-1:j]
        arr.sort()
        ch = arr[k-1]
        answer.append(ch)
        
    return answer