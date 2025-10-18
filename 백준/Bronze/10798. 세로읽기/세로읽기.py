ch = []
result = []
for _ in range(5):
    s= list(input())
    ch.append(s)


for a in range(15):
    for i in range(5):
        try:
            result.append(ch[i][a])
        except:
            continue
    
print(*result, sep='')