n = int(input())
seat = input()

# Write your code here!
arr = []
cnt_val = 0
for i in range (n):
    if seat[i] == "1":
        arr.append(i+1)

for i in range (1, n+1):
    if i in arr:
        continue
    arr2 = arr+[i]
    arr2.sort()
    arr3=[]
    for k in range (len(arr2)-1):
        arr3.append(abs(arr2[k+1]-arr2[k]))
    cnt_val = max(cnt_val, min(arr3))
print(cnt_val)

