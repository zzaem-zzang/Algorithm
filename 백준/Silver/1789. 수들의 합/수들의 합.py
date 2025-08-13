S = int(input())

val = 0
cnt = 0  
while True:
    if S > 0:
        val += 1
        S -= val
        if S< 0:
            break
        cnt+=1
    else:
        break
print(cnt)
