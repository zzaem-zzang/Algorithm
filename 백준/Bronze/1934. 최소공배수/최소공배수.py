import math

T =int(input())
for Tc in range(T):
    a, b = map(int, input().split())
    gcd = math.gcd(a,b) # a와 b의 최대 공약수
    lcm = a * b //gcd
    print(lcm)