def star(n):
    if n == 1:
        return ['*']
    
    arr = star(n//3)
    stars = []

    for i in range(3):
        for j in range(len(arr)):
            if i == 1:
                stars.append(arr[j] + ' ' * (n // 3) + arr[j])
            else:
                stars.append(arr[j] * 3)
    return stars

N = int(input())
print('\n'.join(star(N)))