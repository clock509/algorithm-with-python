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
    values_half1 = values[:middle]
    values_half2 = values[middle:]
    merge_sort(values_half1)
    merge_sort(values_half2)
    
    # 3. 두 배열을 하나로 병합.
    index_values = 0
    while values_half1 and values_half2:
        if values_half1[0] < values_half2[0]:
            values[index_values] = values_half1[0]
            index_values += 1
            values_half1.pop(0)
        else:
            values[index_values] = values_half2[0]
            index_values += 1
            values_half2.pop(0)
            
    # 4. 아직 남아있는 데이터는 결과 배열에 추가.
    while values_half2:
        values[index_values] = values_half2[0]
        values_half2.pop(0)
        index_values += 1
    while values_half1:
        values[index_values] = values_half1[0]
        values_half1.pop(0)
        index_values += 1
        
    return values


print(merge_sort(values)) 