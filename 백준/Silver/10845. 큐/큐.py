N = int(input())
queue= []
for _ in range(N):
    command = list(input().split())
    if command[0] =='push':
        queue.append(command[1])
    elif command[0] =='front':
        if len(queue) >0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] =='back':
        if len(queue) >0:
            print(queue[-1])
        else:
            print(-1)
    elif command[0] =='size':
        print(len(queue))
    elif command[0] =='empty':
        if len(queue)>0:
            print(0)
        elif len(queue) ==0:
            print(1)
    elif command[0]=='pop':
        if len(queue)>0:
           temp = queue.pop(0)
           print(temp)
        else:
            print(-1)
    