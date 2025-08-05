T = int(input())

for Tc in range(T):
    N = int(input())
    arr = [0] * 10
    a = input()

    for i in a:
        arr[int(i)] +=1

    max_val = arr[0]
    idx = 0
    max_num = 0
    for j in range(1,len(arr)):
        if max_val < arr[j]:
            max_val = arr[j]
            idx = j

        elif max_val == arr[j]:
            idx = j

    print(f'#{Tc+1} {idx} {arr[idx]}')



