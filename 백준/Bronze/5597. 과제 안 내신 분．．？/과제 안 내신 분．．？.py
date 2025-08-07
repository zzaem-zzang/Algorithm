sol = []
all = []
for _ in range(28):
    s = int(input())
    sol.append(s)
for i in range(1,31):
    all.append(i)

result = set(all) - set(sol)
for i in sorted(result):
    print(i)