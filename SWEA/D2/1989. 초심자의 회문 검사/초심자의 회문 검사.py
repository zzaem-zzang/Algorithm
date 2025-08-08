T = int(input())

for Tc in range(T):
    ch = input()
    result = 1
    for i in range(len(ch)):

        if ch[i] == ch[len(ch)-i-1]:
            continue
        else:
            result = 0
            break
    print(f'#{Tc+1} {result}')


