lst1 = []
lst2 = set()

for _ in range(10):
    num = int(input())
    lst1.append(num)

for l in lst1:
    result = l % 42
    lst2.add(result)
print(len(lst2))