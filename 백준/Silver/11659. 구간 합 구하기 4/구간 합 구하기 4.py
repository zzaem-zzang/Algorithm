N, M = map(int, input().split()) # n은 수의 개수, m은 구해야 횟수

numbers = list(map(int, input().split()))
total = [0] * (N+1)
total[0] = 0
total[1] =numbers[0]
for i in range(2, N+1):
    total[i] = numbers[i-1] + total[i-1]


for _ in range(M):
    i, j = map(int, input().split())
    result = total[j] - total[i-1]
    print(result)
    
    