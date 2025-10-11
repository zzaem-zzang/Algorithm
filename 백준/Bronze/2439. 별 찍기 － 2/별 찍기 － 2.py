N =int(input())
for n in range(1,N+1):
    p = (n*'*').rjust(N)
    print(p)