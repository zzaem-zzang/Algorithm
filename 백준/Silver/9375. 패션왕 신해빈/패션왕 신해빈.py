T = int(input())

for _ in range(T):
    clothes = {}
    num = int(input())
    for _ in range(num):
        a, b = input().split()
        if b not in clothes:
            clothes[b] = 1
        else:
            clothes[b] +=1
    
    answer = 1
    for cnt in clothes.values():
        answer *= (cnt+1)
    print(answer-1)
        
   