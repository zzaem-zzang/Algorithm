for test_case in range(1, 11):                 
    N = int(input())                          
 
    table = []                                
    for _ in range(N):                         
        row = list(map(int, input().split()))  
        table.append(row)                     
 
    count = 0                                   
    for col in range(N):                       
        flag = False                            #  표시하는 플래그
        for row in range(N):                   
            value = table[row][col]             
            if value == 1:                      # N극 성질의 자성체(아래로 떨어짐)
                flag = True                     # 충돌 후보가 생김 (다음에 2 만나면 교착)
            elif value == 2:                    # S극 성질의 자성체(위로 움직임)
                if flag:                        # 이전에 1이 있었으면 충돌 발생
                    count += 1                  
                    flag = False                # 같은 열에서 다음 교착 상태를 위해 초기화
 
    print("#{} {}".format(test_case, count))    # 테스트 케이스 번호와 교착 상태 수 출력