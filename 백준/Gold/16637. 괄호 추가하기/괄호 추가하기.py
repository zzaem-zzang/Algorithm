# 재귀?
def opera(num1, num2,op):
    if op =='+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op =='*':
        return num1 * num2
    
# 9
# 3+8*7-9*2
# 연산자를 두개씩 비교하면서 크면 괄호 / 아닐경우 순차계산
def sub_set(i, total):
    global max_val

    if i>= N: # 종료조건
        max_val = max(max_val, total)
        return 
    
    # 괄호인것과 아닌것의 최댓값을 찾기
    
    # i)1 괄호 X
    op = string[i-1]
    num = int(string[i])
    sub_set(i+2,opera(total,num,op)) 

    # i)2 괄호 O
    if i+2 < N:
        op1 = string[i-1]
        op2 = string[i+1]    
        num1 = int(string[i])
        num2 = int(string[i+2])
        # 뒤 먼저 계산 op2 먼저
        front = opera(num1,num2,op2)
        sub_set(i+4,opera(total, front, op1))

    


N = int(input())  # 문자열 길이 
string = input() # 식
max_val = float('-inf')
sub_set(2,int(string[0]))
print(max_val)