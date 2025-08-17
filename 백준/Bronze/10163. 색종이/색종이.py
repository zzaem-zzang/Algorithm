T = int(input())
arr = [[0]*101 for _ in range(101)]

for Tn in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x1+x2):
        for j in range(y1, y1+y2):
            arr[i][j] = Tn

for num in range(1, T+1):
    cnt = sum(row.count(num) for row in arr)
    print(cnt)
