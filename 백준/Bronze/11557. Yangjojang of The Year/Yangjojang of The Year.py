T = int(input())

for _ in range(T):
    max_drink = -1
    name= ''
    num = int(input())
    for _ in range(num):
        school, drink = input().split()
        if max_drink < int(drink):
            max_drink = int(drink)
            name= school
    print(name)

