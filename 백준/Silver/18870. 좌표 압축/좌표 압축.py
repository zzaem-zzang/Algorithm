def binary(num):
    st = 0 
    en = len(s_list)-1
    while st <= en:
        mid = (st + en)//2
        if num > s_list[mid]:
            st = mid+1
        elif num < s_list[mid]:
            en = mid-1
        else:
            return mid


N = int(input())
lst = list(map(int,input().split()))
s_list = sorted(set(lst))

for i in lst:
    b = binary(i)
    print(b, end=' ')