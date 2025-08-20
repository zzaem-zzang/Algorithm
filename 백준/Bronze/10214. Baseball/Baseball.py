T = int(input())

for _ in range(T):
    a,b =0,0
    for _ in range(9):
        A, B =map(int, input().split())
        if A>B:
            a+=1
        elif B<A:
            b+=1
    if a>b:
        print('Yonsei')
    elif b>a:
        print('Korea')
    else:
        print('Draw')
