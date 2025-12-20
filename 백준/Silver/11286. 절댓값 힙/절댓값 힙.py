import heapq

N = int(input())

# 작은순부터 힙이 생기므로
heap = []
for _ in range(N):
    num = int(input())
    if num != 0:
        if num < 0:
            heapq.heappush(heap, (abs(num), num)) 
        else:
            heapq.heappush(heap, (num, num))
    else:
        if heap:
            a, b = heapq.heappop(heap)
            print(b)
        else:
            print(0)