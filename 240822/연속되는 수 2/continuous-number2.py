n = int(input())
arr = []
for _ in range (n):
    a = int(input())
    arr.append(a)
cnt = 1
Max = 1
for i in range (len(arr)-1):
    if arr[i]==arr[i+1]:
        cnt+=1
    elif arr[i]!=arr[i+1]:
        cnt=1
    Max = max(Max, cnt)
print(Max)