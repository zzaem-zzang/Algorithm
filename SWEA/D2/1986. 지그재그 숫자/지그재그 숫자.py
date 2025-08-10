T = int(input())

for Tc in range(T):
    num = int(input())
    result = 0
    for i in range(1,num+1):
        if i% 2 == 1:
            result += i
        elif i % 2== 0:
            result -= i
    print(f"#{Tc+1} {result}")
    