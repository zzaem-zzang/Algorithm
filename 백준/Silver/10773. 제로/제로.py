# 재현이는 잘못된 수를 부를때 0을 외쳐  재민이가 쓴 수 지우기
# 즉 0이 아닌 다른 값을 입력하게 되면 스택에 추가되고 0일 경우 스택에 있는 최상단 값 삭제
K = int(input())
stack = []

for _ in range(K):
    s = int(input())
    if s != 0 :
        stack.append(s)
    elif s == 0 :
        stack.pop()
    
print(sum(stack))
