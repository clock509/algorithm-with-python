n = int(input("찾고자 하는 값을 입력하세요: "))
values = [1, 3, 4, 5, 6, 7, 8, 9, 13, 44, 32, 68]


def search_value(values: list, n: int):
    if n not in values:
        return -1
    
    for index, value in enumerate(values):
        if value == n:
            return index
        
print(search_value(values, n))