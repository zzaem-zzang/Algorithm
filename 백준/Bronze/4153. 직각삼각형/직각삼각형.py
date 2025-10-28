
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break

    lst.sort()
    a = lst[0]
    b = lst[1]
    c = lst[2]
    if a**2 + b **2 == c **2:
        print('right')
    else:
        print('wrong')
    