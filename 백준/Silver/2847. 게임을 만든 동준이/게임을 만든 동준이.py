N = int(input())

lst = list()

for _ in range(N):
    num = int(input())
    lst.append(num)

cnt = 0 
for i in range(N-1 ,0, -1):
    if lst[i] <= lst[i-1]:
        cnt += lst[i-1] - lst[i] + 1
        lst[i-1] = lst[i-1] - (lst[i-1]-lst[i] + 1)

print(cnt)

