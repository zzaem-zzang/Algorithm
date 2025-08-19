alphabet = input()
flag = True  # 기본값 True

for i in range(len(alphabet)//2):
    if alphabet[i] != alphabet[-1-i]:  # 틀리면
        flag = False
        break

if flag:
    print(1)
else:
    print(0)
