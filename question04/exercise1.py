"""
# 연습문제
- 1부터 n까지의 합 구하기를 재귀 호출로 만들기.
"""

n = int(input("숫자를 입력하세요: "))


def recursive_summation(number: int) -> int:
    if number <= 0:
        return 0
    
    return number + recursive_summation(number-1)


print(recursive_summation(n))