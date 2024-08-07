class info:
    def __init__(self, name, score):
        self.name = name
        self.score = score
arr = []
for _ in range (5):
    name, score = tuple(input().split())
    infoma = info(name, score)
    arr.append(infoma)
n = int(arr[0].score)
cnt = 0
for i in range (0, 5):
    info_low = int(arr[i].score)
    if n > info_low:
        n = info_low
        cnt = i
    
print(f"{arr[cnt].name} {arr[cnt].score}")