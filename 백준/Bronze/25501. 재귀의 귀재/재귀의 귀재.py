def isPalindrome(string,start,end, cnt = 1):
    
    if start >= end: 
        return 1, cnt
    elif string[start] != string[end]: 
        return 0, cnt
    else: 
        return isPalindrome(string,start+1,end-1, cnt+1)
    

T = int(input())
for Tc in range(1,T+1):
    s = input()
    length = len(s)
    result = isPalindrome(s,0,length-1)
    print(*result)
 