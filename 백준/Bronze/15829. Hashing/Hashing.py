L = int(input())
lst = list(input())
result = 0
for l in range(L):
    temp = ord(lst[l])-96
    result += (31 ** l) * temp
print(result % 1234567891)