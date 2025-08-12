N = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i==0:
            return False
    return True

while True:
    strN = str(N)
    length = len(strN) //2
    flag = True
    for i in range(length):
        if strN[i] != strN[len(strN)-i-1]:
            flag=False
            break
    if flag and is_prime(N):
        print(N)
        break

    N += 1