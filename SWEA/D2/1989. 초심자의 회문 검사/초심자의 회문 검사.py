T = int(input())

for Tc in range(T):
    char = input().strip() # strip을 활용하여 공백제거
    flag = 1
    for i in range((len(char))//2):
        if char[i]  != char[len(char)-i-1]:
            flag = 0
            break
    print(f'#{Tc+1} {flag}')