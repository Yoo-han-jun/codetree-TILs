Max_R = 2001
os = 1000
arr1 = []
arr2 = []
arr = [[0 for _ in range (Max_R)] for _ in range (Max_R)]

for i in range (1,3):
    x1, y1, x2, y2 = map(int,input().split())
    x1, y1, x2, y2 = x1+os, y1+os, x2+os, y2+os
    for j in range (x1, x2):
        for k in range (y1, y2):
            arr[j][k] = i
area = 0
for i in range (len(arr)):
    for j in range (len(arr[i])):
        if arr[i][j] ==1:
            area+=1 
if area == 0:
    print(0)
else:
    for i in range (len(arr)):
        for j in range (len(arr[i])):
            if arr[i][j] == 1:
                arr1.append(i)
                arr2.append(j)
    x = max(arr1)- min(arr1)
    y = max(arr2) - min(arr2)
    print((x+1)*(y+1))