N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write
arr1 = list(set(num))
arr1.sort()
arr2=[]
for i in range (len(arr1)):
    cnt = 0
    for j in range (len(num)):
        if arr1[i]==num[j]:
            cnt+=1
    arr2.append(cnt)
if sum(arr2)==0:
    print(0)
else:
    print(arr1[arr2.index(max(arr2))])
