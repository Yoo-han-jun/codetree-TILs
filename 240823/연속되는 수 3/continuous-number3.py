n = int(input())
arr = []
arr2 = []
for _ in range (n):
    s = int(input())
    if s<0:
        arr.append(-1)
    else:
        arr.append(0)
cnt =0
max_n =0
for i in range (n-1):
    if arr[i] == arr[i+1]:
        cnt+=1
    elif arr[i]!= arr[i+1]:
        cnt = 1
    max_n = max(cnt, max_n)
print(max_n)