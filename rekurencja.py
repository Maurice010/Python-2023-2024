# ZADANIE 4.3
def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

# ZADANIE 4.4
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    prev = 0
    curr = 1
    for i in range(2, n + 1):
        temp = prev + curr
        prev = curr
        curr = temp
    return curr