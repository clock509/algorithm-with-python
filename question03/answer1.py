n = input("이름을 입력하세요(','로 구분): ")
names = n.split(',')


def find_same_name(names: list) -> set:
    same_names = set()
    
    for i in range(len(names)-1): # 마지막 이름은 이전 모든 이름들과 비교가 되었고, 그 뒤로는 더 이상 비교할 이름이 없음.
        for compare_name in names[i+1:]:
            if names[i] == compare_name:
                same_names.add(names[i])
                
    return same_names


print(find_same_name(names))