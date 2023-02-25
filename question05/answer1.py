a = int(input('첫 번째 자연수를 입력하세요: '))
b = int(input('두 번째 자연수를 입력하세요: '))

def get_divisor(number: int) -> set:
    divisors: set = set()
    for num in range(1, number+1):
        if number % num == 0:
            divisors.add(num)
    return divisors


def gcd(a: int, b: int) -> int:
    divisors_a = get_divisor(a)
    divisors_b = get_divisor(b)

    intersection = divisors_a & divisors_b
    return max(list(intersection))
            
            
print(gcd(a, b))