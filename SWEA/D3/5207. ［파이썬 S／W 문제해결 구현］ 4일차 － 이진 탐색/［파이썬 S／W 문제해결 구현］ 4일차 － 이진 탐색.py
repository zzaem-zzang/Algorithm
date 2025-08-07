T = int(input())

for Tc in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    A = sorted(a)
    B = list(map(int, input().split()))
    cnt =0
    arr =[]
    for i in range(len(B)):
        if B[i] > A[(len(A)-1)//2]:
            arr.append('left')
        elif B[i] == A[(len(A)-1)//2]:
            arr.append(' ')
        elif B[i] < A[(len(A)-1)//2]:
            arr.append('right')

    for i in range(len(B)):
        start = 0
        end = len(A) - 1
        dir = arr[i]

        while start <= end :
            mid = (start + end) // 2
            if A[mid] == B[i]:
                cnt +=1
                break
            elif A[mid] > B[i]:
                if dir == 'right':
                    end = mid -1
                    dir ='left'
                else:
                    break

            elif A[mid] < B[i]:
                if dir =='left':
                    start = mid + 1
                    dir ='right'
                else:
                    break

    print(f'#{Tc+1} {cnt}')