"""
# 연습문제
- n명 중 두 명을 뽑아 짝을 짓는다고 할 때, 짝을 지을 수 있는 모든 조합을 출력하는 프로그램을 만들기.
"""

n = input("이름을 입력하세요(','로 구분): ")
names = n.split(',')


def make_pairs(names: list):
    pairs:list = []
    
    for i in range(len(names)-1):
        for compare_name in names[i+1:]:
            if names[i] != compare_name and set([names[i], compare_name]) not in pairs:
                pairs.append(set([names[i], compare_name]))
    return pairs

    # 리스트, 집합 자료형을 쓰지 않고 단순히 출력만 하려면 아래와 같이 한다.
    # for i in range(len(names)-1):
    #     for compare_name in names[i+1:]:
    #         if names[i] != compare_name:
    #             print(f"{names[i]} - {compare_name}")

print(make_pairs(names))