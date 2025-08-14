H, M = map(int, input().split())
if M-45 >=0:
    M= M-45
else:
    H = (H-1)%24
    M = (M+60)-45  
print(H, M)