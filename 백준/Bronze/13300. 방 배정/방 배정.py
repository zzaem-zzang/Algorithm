import math
# 참여 학생수 N  최대 인원수 K
N , K = map(int, input().split())
dict = {}

for i in range(2):
    for j in range(1,7):
        dict[i, j] = 0
# i = 0~1 , j = 1~ 6
for _ in range(N):
    sex, grade =(map(int,input().split()))
    dict[sex, grade] +=1

room = 0
for i in range(2):
    for j in range(1,7):
        room +=  math.ceil(dict[i,j] / K)
     
print(room)