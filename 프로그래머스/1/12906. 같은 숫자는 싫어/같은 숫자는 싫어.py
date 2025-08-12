def solution(arr):
    result = [arr[0]]
    for a in range(1,len(arr)):
        if arr[a] != arr[a-1] :
            result.append(arr[a])
    return result