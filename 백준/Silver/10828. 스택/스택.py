import sys
input = sys.stdin.readline

# N은 명령의 수
N = int(input())
stack = []
top = -1
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        x = command[1]
        top +=1
        stack.append(int(x))
    
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        print(0 if stack else 1)
        
    elif command[0] =='pop':
        if stack:
            print(stack.pop())
            top -=1
        else:
            print(-1)
        