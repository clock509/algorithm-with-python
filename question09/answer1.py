n = input("정렬할 값들을 입력하세요(','로 구분): ")
values = [int(number) for number in n.split(',')]


def insertion_sort(values: list):
    result = []

    while values:
        subject = values.pop()
        new_index = 0
        for i in range(0, len(result)):
            if subject < result[i]:
                new_index = i
            else:
                new_index = len(result)
        result.insert(new_index, subject)
                

    return result
        
print(insertion_sort(values))