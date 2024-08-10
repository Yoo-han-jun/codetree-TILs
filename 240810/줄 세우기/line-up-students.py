class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

arr = []
n = int(input())
for i in range(1, n+1):
    he, we = tuple(input().split())
    stu = Student(int(he),int(we), int(i))
    arr.append(stu)

arr.sort(key=lambda x: (-x.height, -x.weight, x.number)) # 국어 점수 기준 내림차순 정렬

# 정렬 이후 등수별 학생 번호 출력
for idx, stu in enumerate (arr,start=1):
    print(f"{stu.height} {stu.weight} {stu.number}")