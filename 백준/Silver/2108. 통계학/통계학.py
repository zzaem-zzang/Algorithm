from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
lst = sorted(int(input()) for _ in range(N))

# 1. 평균
print(round(sum(lst) / N))

# 2. 중앙값
print(lst[N // 2])

# 3. 최빈값 (여러 개면 두 번째 값)
counter = Counter(lst).most_common()
max_freq = counter[0][1]
modes = [num for num, freq in counter if freq == max_freq]
print(modes[0] if len(modes) == 1 else modes[1])

# 4. 범위
print(lst[-1] - lst[0])
