N = int(input())

for i in range(1,N+1):
    total = list(map(int,str(i)))
    total_sum = sum(total)
    result = total_sum+ i

    if result == N:
        print(i)
        break

else:
    print(0)

