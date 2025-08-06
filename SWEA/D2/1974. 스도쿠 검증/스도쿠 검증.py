T = int(input())

for Tc in range(T):
    arr = []
    for _ in range(9):
        row = list(map(int, input().split()))
        arr.append(row)
    sol = [1,2,3,4,5,6,7,8,9]
    result = 1
    for i in range(0,9,3):
        S = set()
        for j in range(0,9,3):
            for a in range(i,i+3):
                for b in range(j,j+3):
                    S.add(arr[a][b])

            if sorted(list(S)) != sol:
                result = 0

    for i in range(0,9):
        S = set()
        for j in range(0,9):
            S.add(arr[i][j])
        if sorted(list(S)) != sol:
            result =0

    for i in range(0,9):
        S = set()
        for j in range(0,9):
            S.add(arr[j][i])
        if sorted(list(S)) != sol:
            result =0

    print(f'#{Tc+1} {result}')