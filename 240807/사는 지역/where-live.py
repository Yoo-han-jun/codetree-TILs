class save:
    def __init__(self, name, num, loca):
        self.name = name
        self.num = num
        self.loca = loca
arr =[]
arr2 = []
n=int(input())
for _ in range (n):
    df = tuple(input().split())
    user = save(df[0],df[1],df[2])
    arr.append(user)
    arr2.append(user.name)
arr2.sort(reverse=True)
for i in range (0,n):
    if arr[i].name == arr2[0]:
        print(f"name {arr[i].name}")
        print(f"addr {arr[i].num}")
        print(f"city {arr[i].loca}")