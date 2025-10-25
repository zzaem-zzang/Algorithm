def solution(food):
    left = []
    right = []
    for idx, f in enumerate(food[1:], start=1):
        if f >=2:
            half = f//2
            for _ in range(half):
                right.insert(0, str(idx))
                left.append(str(idx))
        else:
            continue
    return ''.join(left) + '0' + ''.join(right)

