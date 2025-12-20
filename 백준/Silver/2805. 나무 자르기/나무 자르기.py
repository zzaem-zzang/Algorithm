# N 나무의수 M 나무의 길이

def cut():
    start = 1
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2
        total = 0 
        for i in trees:
            if i > mid:
                total += i - mid
        if total >= M:
            start = mid + 1
        else:
             end = mid - 1
    return end
    

N, M = map(int ,input().split())
trees = list(map(int, input().split()))
cm = cut()
print(cm)