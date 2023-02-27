"""
# 연습문제 1
- 주어진 리스트와 찾고자 하는 특정 값이 주어질 때, 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘을 만들라.
- 찾는 값이 리스트에 없으면, 빈 리스트를 돌려주게 하라.
"""

n = int(input("찾고자 하는 값을 입력하세요: "))
values = [1, 3, 4, 5, 6, 7, 8, 6, 9, 13, 44, 32, 6, 68]


def search_value(values: list, n: int) -> list: # 계산 복잡도: 비교가 최대 n번 필요하므로 O(n)
    result: list = []
    if n not in values:
        return result
    
    for index, value in enumerate(values):
        if value == n:
            result.append(index)
    
    return result
print(search_value(values, n))