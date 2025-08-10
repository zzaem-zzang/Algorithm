# N 명수 , M 은 받은 횟수 L 은 ~번째
N , M , L = list(map(int,input().split()))
arr = [0]* N
i = 0
arr[i] = 1
total = 0 
while max(arr) < M:
    if arr[i] % 2== 1:
        i = (i + L) % N

    elif arr[i] % 2==0:
        i = (i - L) % N

    arr[i] +=1
    total+=1

print(total)

