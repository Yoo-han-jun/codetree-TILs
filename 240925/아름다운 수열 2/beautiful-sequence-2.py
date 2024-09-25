n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr2.sort()
sum_val=0
for i in range (n-m+1):
    arr3 = []
    for j in range (i, i+m):
        arr3.append(int(arr[j]))
    arr3.sort()
    if arr3 == arr2:
        sum_val+=1
    arr3.clear()
print(sum_val)