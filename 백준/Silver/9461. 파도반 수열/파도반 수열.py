
T = int(input())

for _ in range(T):
    lst= [0] * 101
    num = int(input())
    if num < 4:
        print(1)
        continue
    else:
        lst[1], lst[2], lst[3] = 1, 1, 1
        
        for i in range(4, num + 1):
            lst[i] = lst[i-2] + lst[i-3]
        print(lst[num])
