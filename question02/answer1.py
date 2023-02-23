n = input("비교할 숫자들을 입력하세요(','로 구분): ")
numbers = n.split(',')


def maximum_number(numbers: list):
    maximum_value = 0
    maximum_index = 0
    for index, number in enumerate(numbers):
        if int(number) > maximum_value:
            maximum_value = int(number)
            maximum_index = index
            
    return maximum_value, maximum_index

print(maximum_number(numbers)[0], maximum_number(numbers)[1])