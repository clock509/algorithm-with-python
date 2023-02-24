n = int(input("숫자를 입력하세요: "))


def recursive_factorial(number: int) -> int:
    if number == 0:
        return 1
    
    return number * recursive_factorial(number-1)

print(recursive_factorial(n))