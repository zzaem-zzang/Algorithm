T = int(input())

for Tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    val = ''
    result = -1
    max_val = -1
    for i in range(N-1):
        for j in range(i+1,N):
            val = arr[i] * arr[j]
            val = list(str(val))

            flag = True

            for v in range(len(val)-1):
                if val[v] > val[v+1]:
                    flag = False
                    break
            if flag:
                result =int(''.join(val))
                if max_val < result:
                    max_val = result


    print(f"#{Tc+1} {max_val}") 
