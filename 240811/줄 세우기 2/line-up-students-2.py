n = int(input())
class save:
    def __init__(self, tall, weight, idx):
        self.tall = tall
        self.weight = weight
        self.idx = idx
arr = []
for i in range (n):
    h, w = tuple(input().split())
    stu = save(int(h), int(w), int(i+1))
    arr.append(stu)

arr.sort(key = lambda x : (x.tall, -x.weight))
for ele in arr:
    print(ele.tall, ele.weight, ele.idx)