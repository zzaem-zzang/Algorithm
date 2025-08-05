N = input()
lst = list(map(int,input().split()))
F = int(input())
cnt = 0
for i in lst:
    if i == F:
        cnt +=1

print(cnt)
