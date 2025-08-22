# [None, ,None , None]    value left right

def in_order(node):
    global s
    if node == 0:
        return 
    in_order(tree[node][1])
    s += tree[node][0]
    in_order(tree[node][2])


for Tc in range(1,11):
    N = int(input())
    tree = [[None,0,0] for _ in range(N+1)]
    for i in range(1,N+1):
        command = input().split()
        if len(command) == 2:
            tree[i][0] = command[1]
        if len(command) == 3:
            tree[i][0] = command[1]
            tree[i][1] = int(command[2])
        if len(command) == 4:
            tree[i][0] = command[1]
            tree[i][1] = int(command[2])
            tree[i][2] = int(command[3])
    s = ''
    in_order(1)
    print(f"#{Tc} {s}")
        
