n = input("정렬할 값들을 입력하세요(','로 구분): ") # 6,8,9,3,1,2,5,10,7,4
values = [int(number) for number in n.split(',')]


def quick_sort(values: list, start: int, end: int):
    n = len(values)
    # 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음.
    if n <= 1:
        return
    
    standard = values[int(n/2)]
    index = start
    for i in range(start, int(n/2)):
        if values[i] < standard:
            values[i], values[index] = values[index], values[i]
            index += 1
    values[index], values[int(n/2)] = values[int(n/2)], values[index]
    
    quick_sort(values, start, index-1)  # 기준의 앞부분 정렬
    quick_sort(values, index+1, end)  # 기준의 뒷부분 정렬
    
    # return values

print(quick_sort(values, 0, len(values)-1))