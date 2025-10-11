lst = []
for _ in range(9):
    num = int(input())
    lst.append(num)
sep = ''
max_val = float('-inf')
for i in range(9):
    if max_val<= lst[i]:
        max_val = lst[i]
        sep = i+1

print(max_val)
print(sep)