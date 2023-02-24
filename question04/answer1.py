n = int(input("숫자를 입력하세요: "))


def factorial(number: int) -> int:
    if number == 0:
        return 1
    
    f = 1
    for i in range(1, number+1):
        f *= i
    
    return f

print(factorial(n))