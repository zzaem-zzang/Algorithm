def solution(my_string):
    answer = []
    my_string = list(my_string)
    for i in my_string:
        if i.isnumeric():
            answer.append(int(i))
    answer.sort()
    return answer