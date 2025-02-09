N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write
arr1 = list(set(num))
arr1.sort()
arr3 = []
for i in range (len(arr1)):
    arr2=[]
    cnt = 0
    for j in range (len(num)):
        if arr1[i]==num[j]:
            arr2.append(j)
    for k in range (len(arr2)-1):
        dist = arr2[k+1]-arr2[k]
        if dist<=K:
            cnt+=1
    arr3.append(cnt)
if sum(arr3)==0:
    print(0)
else:
    print(arr1[arr3.index(max(arr3))])
