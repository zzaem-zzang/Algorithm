T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 

for test_case in range(1, T + 1):
    target_count, target_sum = map(int, input().split())
    valid_subset_count = 0 

    for bitmask in range(2**12): 
        subset_count = 0 
        subset_sum = 0   

        for bit in range(12):
            if bitmask & (1 << bit):  
                subset_count += 1
                subset_sum += A[bit]

        if subset_count == target_count and subset_sum == target_sum:
            valid_subset_count += 1

    print(f'#{test_case} {valid_subset_count}')
