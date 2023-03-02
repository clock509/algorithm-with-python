n = input("정렬할 값들을 입력하세요(','로 구분): ") # 6,8,9,3,1,2,5,10,7,4
values = [int(number) for number in n.split(',')]


def merge_sort(values: list):
    n = len(values)
    
    # 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음.
    if n <= 1:
        return values
    
    # 1. divide: 입력 배열을 같은 크기의 2개의 부분 배열로 분할]
    middle = int(n/2)

    # 2. Conquer: 분할된 두 부분 배열을 각각 정렬한다. 부분 배열의 크기가 충분히 작지 않으면, 재귀 호출을 이용해 다시 분할하여 정렬한다.
    values_half1 = merge_sort(values[:middle])
    values_half2 = merge_sort(values[middle:])
    result = []
    while values_half1 and values_half2:
        if values_half1[0] < values_half2[0]: # 내림차순으로 정렬하려면 부등호를 '>'로 바꾼다.
            pick = values_half1.pop(0)
        else:
            pick = values_half2.pop(0)
        result.append(pick)

    # 3. 아직 남아있는 데이터는 결과 배열에 추가.
    while values_half1:
        result.append(values_half1.pop(0))
    while values_half2:
        result.append(values_half2.pop(0))
        
    return result

print(merge_sort(values)) 