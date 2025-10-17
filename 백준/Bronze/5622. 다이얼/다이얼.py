time = 0
phone = input()
num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for i in range(len(num)):
    for p in phone:
        if p in num[i]:
            time += i+3
print(time)