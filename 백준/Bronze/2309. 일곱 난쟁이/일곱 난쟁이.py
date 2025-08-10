arr = []
for _ in range(9):
    arr.append(int(input()))
arr = sorted(arr)
total = sum(arr)

idx1, idx2 = 0 , 0 
for i in range(9):
    for j in range(i+1,9):
        if total - (arr[i] + arr[j]) == 100:
            idx1 = i
            idx2 = j
            break

    
for k in range(9):
    if idx1 != k and idx2 != k :
        print(arr[k])
    
