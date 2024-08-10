class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
arr = []
n = int(input())
for _ in range (n):    
    name, height, weight = tuple(input().split())
    stu = student(name, int(height), int(weight))
    arr. append(stu)

arr.sort(key = lambda x: (x.height, -x.weight))
for ele in arr:
    print(ele.name, ele.height, ele.weight)