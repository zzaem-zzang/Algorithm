n = int(input())
for _ in range(n):
    people = int(input())
    max_name= ''
    max_val = 0
    for _ in range(people):
        price, name = input().split()
        if max_val < int(price):
            max_val= int(price)
            max_name= name
    print(max_name)
