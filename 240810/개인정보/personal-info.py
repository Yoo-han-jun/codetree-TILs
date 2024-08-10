class student:
    def __init__(self, name, heihgt, weight):
        self.name = name
        self.heihgt = heihgt
        self.weight = weight
arr = []
for _ in range (5):
    name, height, weight = tuple(input().split())
    stu = student(name, int(height), float(weight))
    arr.append(stu)
print("name")
arr.sort(key = lambda x: (x.name))
for ele in arr:
    print(ele.name, ele.heihgt, ele.weight)
print()
print("height")
arr.sort(key = lambda x: (-x.heihgt))
for ele in arr:
    print(ele.name, ele.heihgt, ele.weight)