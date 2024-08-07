class bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
df = tuple(input().split())
info = bomb(df[0],df[1],int(df[2]))
print(f"code : {info.code}")
print(f"color : {info.color}")
print(f"second : {info.second}")