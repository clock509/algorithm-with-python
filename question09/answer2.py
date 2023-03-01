n = input("정렬할 값들을 입력하세요(','로 구분): ")
values = [int(number) for number in n.split(',')]


def insertion_sort(values: list):
    n = len(values)
    
    for i in range(1, n):
        value = values[i]
        j = i - 1
        while j >= 0 and values[j] > value:  # 내림차순 정렬하려면 values[j] < value 로 부등호 방향 변경
            values[j+1] = values[j]
            j -= 1
        values[j+1] = value
    
    return values
print(insertion_sort(values))