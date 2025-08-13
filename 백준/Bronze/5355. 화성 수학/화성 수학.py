def sum_total(*maths):
    num = float(maths[0])
    for i in range(1,len(maths)):
        if maths[i]=='@':
            num *=3
        elif maths[i] =='%':
            num += 5
        elif maths[i] =='#':
            num -=7 
    return num

T = int(input())
for Tc in range(T):
    maths = input().split()
    total =sum_total(*maths)
    print(f'{total:.2f}')