"""
# 연습문제 2
- 다음과 같이 학생 번호와 이름이 리스트로 주어졌을 때, 학생 번호를 입력히면 그에 해당한느 이름을 순차 탐색으로 찾아 돌려주는 함수를 만들라.
- 해당하는 학생 번호가 없으면, "?"를 돌려주게 하라.
"""

n = int(input("찾고자 하는 학생의 번호를 입력하세요: "))


def search_student_by_number(n: int) -> list: # 계산 복잡도: 비교가 n번 필요하므로 O(n)    
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]
    
    if n not in stu_no:
        return "?"
    
    for index, number in enumerate(stu_no):
        if number == n:
            return stu_name[index]
    
print(search_student_by_number(n))