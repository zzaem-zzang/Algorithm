T = int(input())
# int( 변수, 2) 2진법을 10진법을 바꾸어줌
for Tc in range(T):
    bin_str = input()  # 2진수 문자열
    thd_str = input()  # 3진수 문자열
    b = []  
    t = []
    
    for i in range(len(bin_str)):
        if bin_str[i] == '0':
            temp = bin_str[:i] + '1' + bin_str[i+1:]
        else:
            temp = bin_str[:i] + '0' + bin_str[i+1:]
        s = int(temp, 2)
        b.append(s)
    
    for i in range(len(thd_str)):
        if thd_str[i] == '0':
            for d in ['1', '2']:
                temp = thd_str[:i] + d + thd_str[i+1:]
                s = int(temp, 3)
                t.append(s)
        elif thd_str[i] == '1':
            for d in ['0', '2']:
                temp = thd_str[:i] + d + thd_str[i+1:]
                s = int(temp, 3)
                t.append(s)
        elif thd_str[i] == '2':
            for d in ['0', '1']:
                temp = thd_str[:i] + d + thd_str[i+1:]
                s = int(temp, 3)
                t.append(s)
    
    for i in b:
        for j in t:
            if i==j:
                result =i
                print(f'#{Tc+1} {i}')
                    
