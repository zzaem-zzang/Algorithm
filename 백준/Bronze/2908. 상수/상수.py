A, B = input().split()
a=''
b=''
for i in range(len(A)-1,-1,-1):
    a += A[i]

for j in range(len(B)-1,-1,-1):
    b += B[j]
a = int(a)
b = int(b)
if a>b:
    print(a)
else:
    print(b)