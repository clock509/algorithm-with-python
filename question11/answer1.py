n = input("정렬할 값들을 입력하세요(','로 구분): ") # 6,8,9,3,1,2,5,10,7,4
values = [int(number) for number in n.split(',')]


def quick_sort(values: list):
    n = len(values)
    
    if n <= 1:
        return values
    
    # 주어진 리스트에서 기준값을 정한다.
    standard = values[int(n/2)] # 임의로 중간번째 값을 기준값으로 정한다.
    
    # 나머지 리스트에서 기준보다 작은 값, 큰 값을 각각 별도의 리스트로 나눈다.
    smaller_value = []
    bigger_value = []
    for i in range(len(values)):
        if values[i] > standard:
            bigger_value.append(values[i])
        elif values[i] < standard:
            smaller_value.append(values[i])
            
    # 각 리스트 안에서 정렬한 후, 작은 값들의 리스트 + 기준 + 큰 값들의 리스트를 합친다.
    return quick_sort(smaller_value) + [standard] + quick_sort(bigger_value)

print(quick_sort(values)) 