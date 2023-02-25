"""
# 연습문제
- 피보나치 수열을 재귀 호출로 만들기.
    - 피보나치 수열: 0과 1부터 시작해서 바로 앞의 두 수를 더한 값을 다음 값으로 추가하는 방식으로 만든 수열.
    - (ex) 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....
- 피보나치 수열이 리스트처럼 0번부터 시작한다고 가정할 때, n번째 피보나치 수를 구하는 알고리즘을 재귀호출을 이용해 구현해 보라.
"""

n = int(input("수열의 몇 번째 수가 궁금한가요? : "))
initial_fibonacci_numbers = [0, 1]

def nth_number_of_fibonacci_numbers(numbers: list, n: int) -> int:
    if n < 2:
        return numbers[n]
    
    new_number = numbers[-2] + numbers[-1]
    if n == len(numbers):
        return new_number
    else:
        numbers.append(new_number)
        return nth_number_of_fibonacci_numbers(numbers, n)

print(nth_number_of_fibonacci_numbers(initial_fibonacci_numbers, n))



"""
# 해답
"""
# def fibonacci(n: int) -> int:
#     if n < 2:
#         return n  # 피보나치 수열은 n == 0 -> 0, n == 1 -> 1
#     return fibonacci(n-2) + fibonacci(n-1) # n번째 수 = n-1번째 수 + n-2번째 수(단, n>=2)
# print(fibonacci(n))