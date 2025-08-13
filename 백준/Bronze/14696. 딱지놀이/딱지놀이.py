def play(A,B):
    A_arr = [0] * 4
    B_arr = [0] * 4

    for i in range(len(A)):
        if A[i] == 4:
            A_arr[0] += 1
        elif A[i] == 3:
            A_arr[1] += 1
        elif A[i] == 2:
            A_arr[2] += 1
        elif A[i] == 1:
            A_arr[3] += 1

    for i in range(len(B)):
        if B[i] == 4:
            B_arr[0] += 1
        elif B[i] == 3:
            B_arr[1] += 1
        elif B[i] == 2:
            B_arr[2] += 1
        elif B[i] == 1:
            B_arr[3] += 1
    
    for i in range(4):
        if A_arr[i] > B_arr[i]:
            return 'A'
        elif A_arr[i] < B_arr[i]:
            return 'B'
    return 'D'
            

T = int(input())
for Tc in range (T):
    A = list(map(int,input().split()))[1:]
    B = list(map(int,input().split()))[1:]
    result = play(A,B)
    print(result)