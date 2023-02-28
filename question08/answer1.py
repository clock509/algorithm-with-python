n = input("정렬할 값들을 입력하세요(','로 구분): ")
values = [int(number) for number in n.split(',')]


def selection_sort(values: list):
    result = []
    
    while values:
        # 1. 가장 작은 값의 인덱스 찾기
        minimum_index = 0
        for i, n in enumerate(values):
            if values[minimum_index] > n:
                minimum_index = i
        
        # 2. 해당 값을 따로 변수에 저장하여 결과 배열에 더하고, 기존 배열에서는 지움.
        minimum_value = values[minimum_index]
        del values[minimum_index]
        result.append(minimum_value)
    
    return result
        
print(selection_sort(values))