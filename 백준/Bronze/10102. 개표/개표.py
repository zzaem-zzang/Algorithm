V = int(input())
Vvote = input()
a , b = 0 , 0
for i in Vvote:
    if i =='A':
        a += 1
    elif i =='B':
        b += 1
if a>b:
    print('A')
elif b>a:
    print('B')
else:
    print('Tie')