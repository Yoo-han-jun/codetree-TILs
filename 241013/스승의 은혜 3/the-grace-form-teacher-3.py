n, b = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range (n)]
arr.sort(key = lambda x:(x[0]//2+x[1],x[0]+x[1],x[1]))
sum_val = 0
arr3 = []
for i in range (n):
    arr1 = [0 for _ in range (n)]
    arr2 = [0 for _ in range (n)]
    for j in range (i):
        p, d = arr[j]
        arr1[j] = int(p)
        arr2[j] = int(d)
    predict = sum(arr1)+sum(arr2)
    if predict>b:
        for j in range (i):
            if arr1[j] == max(arr1):
                arr1[j] = arr1[j]//2
                break
    predict = sum(arr1)+sum(arr2)
    if predict>b:
        arr3.append(i)
if arr3:
    print(min(arr3)-1)
else:
    print(n)