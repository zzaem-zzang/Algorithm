T = int(input())

for _ in range(T):
    input_numbers = list(map(int, input().split()))
    even_numbers = []
    
    for i in input_numbers:
        if i % 2 == 0:
            even_numbers.append(i) 
    
    print(sum(even_numbers), min(even_numbers))