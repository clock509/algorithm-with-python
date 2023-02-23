n = input("비교할 숫자들을 입력하세요(','로 구분): ")
# nums = [int(number) for number in n]
numbers = n.split(',')

sorted_numbers = sorted(numbers, key=lambda x: int(x))

print(sorted_numbers[-1])
# maximum = 0
# for number in numbers:
#     if int(number) > maximum:
#         maximum = int(number)

# print(maximum)