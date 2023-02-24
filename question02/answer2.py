n = input("비교할 숫자들을 입력하세요(','로 구분): ")
numbers = n.split(',')

sorted_numbers = sorted(numbers, key=lambda x: int(x))

print(sorted_numbers[-1])