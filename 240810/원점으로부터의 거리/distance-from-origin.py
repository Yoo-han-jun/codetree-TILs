class distance:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
arr = []
n = int(input())
for i in range(1,n+1):
    x, y = tuple(input().split())
    dot = distance(int(x),int(y), int(i))
    arr.append(dot)

arr.sort(key = lambda x:((abs(x.x) + abs(x.y)), x.number))
for ele in arr:
    print (ele.number)