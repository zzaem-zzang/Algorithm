T = int(input())
for Tc in range(T):
    num, S = input().split()
    for i in range(len(S)):
        print(f"{S[i] * int(num)}", end='')
    print()