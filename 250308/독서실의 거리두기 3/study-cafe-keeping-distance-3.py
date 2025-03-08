N = int(input())
seats = input()
arr=[]
arr2=[]
# Please write your code here.
for i in range (N):
    if int(seats[i])==1:
        arr.append(i)
for i in range (len(arr)-1):
    arr2.append(arr[i+1]-arr[i])
num = arr2.index(max(arr2))

min_cnt = 1000
if arr[num]!=2:
    for j in range ((arr[num]+arr[num+1])//2,(arr[num]+arr[num+1])//2+1 ):
        arr3 = [j]
        arr4 = []
        for i in range (N):
            if int(seats[i])==1:
               arr3.append(i)
        arr3.sort()        
        for i in range (len(arr3)-1):
            k = arr3[i+1]-arr3[i]
            arr4.append(k)
        min_cnt = min(min(arr4), min_cnt)
elif arr[num]==2:
    min_cnt = 1
min_cnt = min(min(arr2), min_cnt)
print(min_cnt)
