"""
# 연습문제
- n개의 숫자 중 최댓값 찾기를 재귀 호출로 만들기.
"""

n = input("비교할 숫자들을 입력하세요(','로 구분): ")
numbers = n.split(',')


def find_maximum_recursively(first_number: int, numbers: list) -> int:
    if len(numbers) <= 1:
        if first_number > numbers[0]:
            return first_number
        else:
            return numbers[0]
    
    if first_number > numbers[0]:
        return find_maximum_recursively(first_number, numbers[1:])
    else:
        return find_maximum_recursively(numbers[0], numbers[1:])


print(find_maximum_recursively(numbers[0], numbers))