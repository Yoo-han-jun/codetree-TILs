class save:
    def __init__(self, number, idx):
        self.number = number
        self.idx = idx
class save2:
    def __init__(self, number, idx, reidx):
        self.number = number
        self.idx = idx
        self.reidx = reidx
n = int(input())
arr = tuple(input().split())
arr2 = []
for i in range(0, n):
    df = save(int(arr[i]), int(i+1))
    arr2.append(df)
cnt = 1
arr3 = []
arr2.sort(key = lambda x : x.number)
for ele in arr2:
    df2 = save2(ele.number, ele.idx, cnt)
    cnt+=1
    arr3.append(df2)

arr3.sort(key = lambda x: x.idx)
for ele in arr3:
    print(ele.reidx, end=" ")