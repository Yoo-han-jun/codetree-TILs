a, b = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
cnt=0
for i in range (a-b+1):
    if arr1[i:i+b] == arr2:
        cnt+=1
if cnt>0:
    print("Yes")
else:
    print("No")