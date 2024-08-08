n = int(input())
class save:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
arr = []
for _ in range(n):
    name, kor, eng, math = tuple(input().split())
    student = save(name, int(kor), int(eng), int(math))
    arr.append(student)

arr.sort(key=lambda x: (-x.kor, -x.eng, -x.math))
for ele in arr:
    print(ele.name, ele.kor, ele.eng, ele.math)