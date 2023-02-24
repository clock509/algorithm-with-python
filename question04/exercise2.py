"""
# 연습문제
- n개의 숫자 중 최댓값 찾기를 재귀 호출로 만들기.
"""

n = input("비교할 숫자들을 입력하세요(','로 구분): ")
numbers = n.split(',')
# numbers = [int(n) for n in numbers]


def find_maximum_recursively(numbers: list, first_number: int) -> int:
    """_summary_
    최초 실행 시 숫자 리스트의 0번째 숫자를 가장 큰 것으로 간주하고, 그것을 제외한 나머지 숫자들과 하나씩 비교하면서 최댓값을 찾아나가는 흐름이다.
    
    Args:
        numbers (list): 입력받은 숫자 전체를 담은 리스트
        first_number (int): 최초에는 리스트 중 0번째 숫자를 전달하며, 함수가 재귀호출 될 때는 현재 가장 큰 숫자를 전달한다.

    Returns:
        int: _description_
    """
    # 종료 조건: 리스트에 숫자가 1개만 남으면 numbers의 마지막 숫자와 first_number를 비교한다.
    if len(numbers) <= 1:
        if first_number > numbers[0]:
            return first_number
        else:
            return numbers[0]
    
    # first_number와 numbers의 0번째 인덱스를 비교한 후, 그 결과에 따라 함수를 다시 호출한다.
    # 다시 호출할 때는, 첫 번째 인자에는 이미 비교가 끝난 numbers 배열의 0번째 숫자는 제외한 나머지 숫자들을 담은 리스트를 전달한다.
    # 두 번째 인자에는 first_number와 numbers 배열의 0번째 숫자 중 더 큰 것을 넣는다.
    if first_number > numbers[0]:
        return find_maximum_recursively(numbers[1:], first_number)
    else:
        return find_maximum_recursively(numbers[1:], numbers[0])


print(find_maximum_recursively(numbers, numbers[0]))