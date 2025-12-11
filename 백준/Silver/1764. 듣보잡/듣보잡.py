N, M = map(int, input().split())

lst1 = []
lst2 = []

for _ in range(N):
    name = input()
    lst1.append(name)

for _ in range(M):
    name = input()
    lst2.append(name)

lst3 = set(lst1) & set(lst2)
lst3 = sorted(lst3)
print(len(lst3))
for a in lst3:
    print(a)