class save:
    def __init__ (self, name, tall, weight):
        self.name = name
        self.tall = tall
        self.weight = weight

n = int(input())
arr = []
for _ in range(n):
    df = tuple(input().split())
    info = save(df[0], df[1], df[2])
    arr.append(info)

arr.sort(key=lambda x: x.tall)
for ele in arr:
    print(ele.name, ele.tall, ele.weight)