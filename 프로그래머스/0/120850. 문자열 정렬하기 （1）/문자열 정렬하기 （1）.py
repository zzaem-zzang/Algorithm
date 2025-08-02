def solution(my_string):
    answer = []

    for ch in my_string:
        if ch.isnumeric():         
            answer.append(int(ch))   # 숫자면 정수로 변환해서 리스트에 추가

    answer.sort()                    # 오름차순 정렬
    return answer
