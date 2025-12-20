
def cut():
    
    start = 1
    end = max(lst)

    while start <= end:
        total = 0
        mid = (start + end) // 2
        for l in lst:
            total += l // mid
            if total >= N:
                break
        if total >= N:
            start = mid + 1
        else:
            end = mid - 1
    print(end)



# 랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
cut()