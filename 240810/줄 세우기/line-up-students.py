class Student:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

arr = []
n = int(input())
for _ in range(n):
    he, we = tuple(input().split())
    stu = Student(int(he),int(we))
    arr.append(stu)

arr.sort(key=lambda x: (x.height, x.weight)) # 국어 점수 기준 내림차순 정렬

# 정렬 이후 등수별 학생 번호 출력
for idx, stu in reversed(list(enumerate (arr,start=1))):
    print(f"{stu.height} {stu.weight} {idx}")