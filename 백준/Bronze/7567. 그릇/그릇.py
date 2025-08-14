glass = input()
total = 10
for i in range(1,len(glass)):
    if glass[i]== glass[i-1]:
        total += 5
    else:
        total += 10
print(total)