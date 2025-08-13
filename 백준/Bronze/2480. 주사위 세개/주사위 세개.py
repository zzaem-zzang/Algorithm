A, B, C = map(int, input().split())
reward = 0

if A == B == C:
    reward = 10000 + A * 1000
elif A != B and B != C and A != C:  # 모두 다른 경우
    # A != B != C 안되는 이유 : A랑 B랑 다르더라도 A랑C가 같을 수 있음
    reward = max(A, B, C) * 100
else:
    if A == B:
        reward = 1000 + A * 100
    elif B == C:
        reward = 1000 + B * 100
    elif A == C:
        reward = 1000 + A * 100

print(reward)
