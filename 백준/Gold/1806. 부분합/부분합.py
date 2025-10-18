import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
result = 0
answer = float('inf')

while left < N:  
    if result >= S:
        answer = min(answer, right - left)
        result -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        result += arr[right]
        right += 1

print(0 if answer == float('inf') else answer)
