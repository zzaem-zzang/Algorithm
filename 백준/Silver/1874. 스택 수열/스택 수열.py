# 스택에다가 push하는 순서를
n = int(input())

stack= []
cnt =1
sol = []
flag = True
for _ in range(n):
    num = int(input()) 
    while cnt <= num:
        stack.append(cnt)
        sol.append('+')
        cnt +=1  # 입력한 값보다 작으면 계속 1씩 더하면서 스택에 넣는다
    if stack and stack[-1]== num:
        sol.append('-')
        stack.pop()

    else:
        flag = False

if flag:
    for i in range(len(sol)):
        print(sol[i])
else:
    print('NO')

    