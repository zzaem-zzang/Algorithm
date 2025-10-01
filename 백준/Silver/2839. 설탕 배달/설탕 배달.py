N = int(input())
result = float('inf')

n = N // 5
for i in range(n, -1, -1):
    remain = N - (i * 5)
    if remain % 3 == 0:   # 남은 무게가 3으로 나눠떨어지면
        bag = i + remain // 3
        result = min(result, bag)

print(-1 if result == float('inf') else result)
