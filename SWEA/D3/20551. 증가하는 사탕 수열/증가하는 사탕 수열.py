T = int(input())

for Tc in range(T):
    A, B, C = map(int, input().split())
    cnt = 0 
    result = -1

    while B>=C:
        B-=1
        cnt += 1

    while A>=B:
        A-=1
        cnt +=1

    if A>0 and B > 0 and C>0 and A<B<C:
        result = cnt
    
    print(f'#{Tc+1} {result}')
