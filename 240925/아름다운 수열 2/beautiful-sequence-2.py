n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
sum_val=0
for i in range (n-m+1):
    arr3 = [0 for _ in range (m)]
    for j in range (i, i+m):
        for l in range (3):
            if arr2[l] == arr[j]:
                arr3[l] = arr2[l]
    if arr3 == arr2:
        sum_val+=1
print(sum_val)