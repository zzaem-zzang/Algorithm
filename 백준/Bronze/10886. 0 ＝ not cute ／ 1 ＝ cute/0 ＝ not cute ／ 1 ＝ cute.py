N = int(input())
arr =[]
not_cute = 0
cute = 0
for _ in range(N):
    arr.append(input())
for i in arr:
    if i=='0':
        not_cute+=1
    elif i =='1':
        cute+=1
if not_cute<cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')