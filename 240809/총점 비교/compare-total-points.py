class student:
    def __init__(self, name, sc1, sc2, sc3):
        self.name = name
        self.sc1 = sc1
        self.sc2 = sc2
        self.sc3 = sc3
arr = []
n = int(input())
for _ in range (n):
    name, sc1, sc2, sc3 = tuple(input().split())
    arr.append(student(name, int(sc1), int(sc2), int(sc3)))
arr.sort(key = lambda x: x.sc1 + x.sc2 + x.sc3)

for ele in arr:
    print(ele.name, ele.sc1, ele.sc2, ele.sc3)