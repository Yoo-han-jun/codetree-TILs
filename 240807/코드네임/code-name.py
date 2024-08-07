class info:
    def __init__(self, name, score):
        self.name = name
        self.score = score
arr = []
for _ in range (5):
    name, score = tuple(input().split())
    infoma = info(name, score)
    arr.append(infoma)

info_low = arr[0]
print(f"{info_low.name} {info_low.score}")