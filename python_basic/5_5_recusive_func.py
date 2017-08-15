#재귀함수 예제

def factorial(n):
    if(n is 1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
