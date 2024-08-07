class Test:
    def __init__(self, code, loca, time):
        self.code = code
        self.loca = loca
        self.time = time
df = tuple(input().split())
Test1 = Test(df[0],df[1],df[2])
print("secret code :", Test1.code)
print("meeting point :", Test1.loca)
print("time :", Test1.time)