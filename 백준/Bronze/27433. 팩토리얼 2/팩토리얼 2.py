def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)

N = int(input())
result = factorial(N)
print(result)

