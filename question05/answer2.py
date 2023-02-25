a = int(input('첫 번째 자연수를 입력하세요: '))
b = int(input('두 번째 자연수를 입력하세요: '))

def gcd(a: int, b: int) -> int:
    divisor = min(a, b)

    while True:    
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        else:
            divisor -= 1
            
            
print(gcd(a, b))