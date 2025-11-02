import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

cnt = 0
left, right = 0, n-1

while left < right:
    s = arr[left]+ arr[right]
    if s == x :
        cnt +=1
        left +=1
        right -=1 
    elif s < x:
        left +=1
    elif s > x:
        right -=1

print(cnt)