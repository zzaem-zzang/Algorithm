T = int(input())
for Tc in range(T):
    sol = input()
    total = 0
    score= 1
    for i in sol:
        if i =='O':
            total += score
            score += 1
        else:
            score =1
    print(total)