N, M = map(int, input().split())
arr =[]
for _ in range(N):
    num = int(input())
    arr.append(num)
arr.sort()

left = 0
right = 0
minval = float('inf')

while right< N:
    diff = arr[right]-arr[left]
    if diff >= M:
        minval = min(diff, minval)
        left += 1
    else:
        right += 1
    
    if left == right:
        right+=1
print(minval)