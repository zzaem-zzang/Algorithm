for T in range(1,11):
    B = int(input())
    heigh = list(map(int, input().split()))
 
    cnt = 0
 
    for i in range(2, B-2):
        pos = heigh[i]
 
        max_val = heigh[i-1]
        if max_val < heigh[i-2]:
            max_val = heigh[i-2]
 
        if max_val < heigh[i+1]:
            max_val = heigh[i+1]
 
        if max_val < heigh[i+2]:
            max_val = heigh[i+2]
 
        if pos > max_val:
            cnt += pos - max_val
    print(f'#{T} {cnt}')