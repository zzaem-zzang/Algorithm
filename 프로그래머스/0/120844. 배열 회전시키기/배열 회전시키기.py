from collections import deque
# deque를 사용할때 양수는 오른쪽 회전 음수는 왼쪽회전

def solution(numbers, direction):
    answer = []
    numbers = deque(numbers)
    
    if direction == 'right':
        numbers.rotate(1)
    elif direction == 'left':
        numbers.rotate(-1)
    return list(numbers)