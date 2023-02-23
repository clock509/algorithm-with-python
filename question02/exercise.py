"""
# 연습문제
- 숫자 n 개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들기.
"""
n = input("비교할 숫자들을 입력하세요(','로 구분): ")
# nums = [int(number) for number in n]
numbers = n.split(',')


def minimum_number(numbers: list):
    minimum_value = int(numbers[0])
    for index, number in enumerate(numbers):
        if int(number) < minimum_value:
            minimum_value = int(number)
            
    return minimum_value

print(minimum_number(numbers))