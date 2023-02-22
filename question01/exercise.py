"""
# 연습문제
- 1부터 n 까지의 연속한 숫자의 제곱의 합을 구하는 프로그램을 for문을 이용해 만들기.
"""
n = int(input("n을 입력하세요: "))

sum = 0
for i in range(1, n+1):
    sum += i ** 2

print(sum)