for Tc in range(1,11):
    dumps = int(input())
    block = list(map(int, input().split()))

    while dumps >0:
        dumps -=1
        min_val = 101
        max_val = -1
        max_idx = -1
        min_idx = -1
        for i in range(len(block)):
            if block[i]> max_val:
                max_val = block[i]
                max_idx = i

            if block[i] < min_val:
                min_val = block[i]
                min_idx = i

        block[max_idx] -= 1
        block[min_idx] += 1

        final_max = -1
        final_min = 101
        for h in block:
            if h > final_max:
                final_max = h
            if h < final_min:
                final_min = h

        result = final_max - final_min

    print(f'#{Tc} {result}')




