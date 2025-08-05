num = input()

lst = [0] * 10

for i in num:
    lst[int(i)] +=1

six_nine = lst[6] + lst[9]
lst[6] = lst[9] = int((six_nine+1)/2)

print(max(lst))
