n = int(input())
arr = list(map(int, input().split()))
arr1 = []
arr2 = []
arr3 = []
# Please write your code here.
for i in range (n):
    if arr[i]>0:
        arr1.append(arr[i])
    if arr[i]<0:
        arr2.append(arr[i])
    if arr[i]==0:
        arr3.append(arr[i])
arr1.sort()
arr1.reverse()
arr2.sort()
arr3.sort()
cnt = 0
if n==3:
    print(arr[1]*arr[0]*arr[2])
elif len(arr2)>=2 and len(arr1)>=2:
    cnt = max(arr2[0]*arr1[0]*arr1[1], arr2[0]*arr2[1]*arr1[0])
elif len(arr2)>=2 and len(arr1)==1:
    cnt = arr2[0]*arr2[1]*arr1[0]
elif len(arr2)>=2 and len(arr1)==0:
    arr2.reverse()
    cnt = arr2[0]*arr2[1]*arr1[2]
elif len(arr2)==1 and len(arr1)==2:
    arr1.reverse()
    cnt = arr2[0]*arr1[0]*arr1[1]
elif len(arr2)<=1 and len(arr1)>=3:
    cnt = arr1[2]*arr1[0]*arr1[1]
elif len(arr2)<2 and len(arr1)<2:
    cnt = 0

if cnt<0 and len(arr3)!=0:
    if n!=3:
        print(0)
else:
    if n!=3:
        print(cnt)

