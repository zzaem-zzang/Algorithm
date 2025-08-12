# 값같은 경우에는 같은 값이 여러개 존재할 수 있음
# 그러므로 인덱스를 기준으로 값을 찾아 나간다.
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
sol = [-1] * N

stack.append(0)
for i in range(1,N):
    while stack and arr[stack[-1]] < arr[i]:
        idx =stack.pop()
        sol[idx] = arr[i]
    stack.append(i)

print(*sol)
