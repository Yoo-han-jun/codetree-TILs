n, k, p, t = map(int,input().split())
class ex:
    def __init__ (self, t, x, y):
        self.t, self.x, self.y = t, x, y

arr = [0]*n
arr2 = [0]*n
arr[p] = 1
arr3 = []
for _ in range (t):
    t, x, y = tuple(input().split())
    pl = ex(int(t), int(x), int(y))
    arr3.append(pl)
arr3.sort(lambda x: x.t)
cnt = 0
for ele in arr3:
    arr2[ele.x-1]+=1
    arr2[ele.y-1]+=1
    if arr[ele.x-1] ==1 and arr2[ele.x-1]<=k:
        arr[ele.y-1] =1
    if arr[ele.y-1] == 1 and arr2[ele.y-1]<=k:
        arr[ele.x-1] =1
for ele in arr:
    print(ele, end="")