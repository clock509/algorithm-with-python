a = int(input('첫 번째 자연수를 입력하세요: '))
b = int(input('두 번째 자연수를 입력하세요: '))

def gcd(a: int, b: int) -> int:
    bigger = max(a, b)
    smaller = min(a, b)
    
    # 어떤 수 n과 0의 최대공약수는 n이다. 즉, gcd(n, 0) = n
    if smaller == 0:
        return bigger
    
    remainder = bigger % smaller
    if remainder == 0:
        return smaller
    else:
        return gcd(smaller, remainder)
    
print(gcd(a, b))