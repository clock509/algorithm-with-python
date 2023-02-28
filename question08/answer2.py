n = input("정렬할 값들을 입력하세요(','로 구분): ")
values = [int(number) for number in n.split(',')]


def selection_sort(values: list): 
    # 이중 반복문 활용: 0번부터 n-1번까지의 숫자 하나 vs 해당 값의 인덱스보다 뒤에 위치한 수들을 비교
    for i in range(len(values)-1):
        for j in range(i+1, len(values)):
            # i가 최소값의 인덱스라고 가정할 때, i 이후의 j번째 값이 i번째 값보다 작다면 서로 위치를 바꿔준다.
            # 만약 내림차순으로 정렬하고자 한다면, if values[i] < values[j]: 로 부등호의 방향이 바뀌어야 한다.
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]
    return values
        
print(selection_sort(values))