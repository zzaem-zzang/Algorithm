def calculate(cnt, temp):
    global min_val
    global max_val

    if num_cnt-1 == cnt:
        max_val = max(max_val, temp)
        min_val = min(min_val, temp)
        return
    nxt = cnt +1
    # +인 경우
    if cal[0] !=0:
        cal[0] -= 1
        calculate(nxt, temp + num_list[nxt])
        cal[0] += 1
    # -인 경우
    if cal[1] !=0:
        cal[1] -= 1
        calculate(nxt, temp - num_list[nxt])
        cal[1] += 1
    # * 인 경우
    if cal[2] !=0:
        cal[2] -= 1
        calculate(nxt, temp * num_list[nxt])
        cal[2] += 1
    # // 인 경우
    if cal[3] !=0:
        cal[3] -= 1
        calculate(nxt, div(temp, num_list[nxt]))
        cal[3] += 1

def div(a,b):
    if (a <0 and b>0) or (a>0 and b<0):
        return -(abs(a) // abs(b))
    elif a>0 and b>0:
        return a //b
    else:
        return abs(a) // abs(b)
    
# 숫자개수
num_cnt = int(input())
# 값
num_list = list(map(int,input().split()))
# 연산자 + - * /
cal = list(map(int,input().split()))
min_val = 10**18
max_val = -10**18
cnt = 0

calculate(cnt, num_list[0])

print(max_val)
print(min_val)
