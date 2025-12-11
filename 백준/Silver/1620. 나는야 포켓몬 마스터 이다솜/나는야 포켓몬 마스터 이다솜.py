N, M = map(int, input().split())

pocket = {}
reverse_pocket = {}

for i in range(N):
    name = input()
    pocket[i+1] = name
    reverse_pocket[name] = i+1
    # 포켓몬 이름 저장 완료

for _ in range(M):
    answer = input()
    if answer[0].isdigit():
        answer = int(answer)
        print(pocket[answer])
    else:
        print(reverse_pocket[answer])