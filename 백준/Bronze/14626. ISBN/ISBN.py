s = input().strip()  

total = 0
weight = None  

for i in range(13):
    ch = s[i]
    
    if ch.isdigit():   # 정상 숫자
        digit = int(ch)
        if i % 2 == 0:
            total += digit
        else:
            total += 3 * digit
    else:
        # 빠진 글자 발견
        if i % 2 == 0:
            weight = 1
        else:
            weight = 3

# 빠진 자리 채우기
if weight == 1:
    for x in range(10):
        if (total + x) % 10 == 0:
            print(x)
            break
else:
    for x in range(10):
        if (total + 3*x) % 10 == 0:
            print(x)
            break
