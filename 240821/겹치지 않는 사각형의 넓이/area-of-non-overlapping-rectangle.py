arr = [[0 for _ in range (2001)] for _ in range (2001)]
os = 1000
cnt = 0
for _ in range (2):
    x1, y1, x2, y2 = map(int,input().split())
    x1, y1, x2, y2 = x1+os,y1+os,x2+os,y2+os 
    for i in range (x1, x2):
        for j in range (y1, y2):
            arr[i][j] = 1

x1, y1, x2, y2 = map(int,input().split())
x1, y1, x2, y2 = x1+os,y1+os,x2+os,y2+os 
for i in range (x1, x2):
    for j in range (y1, y2):
        arr[i][j] = 0

for i in range (len(arr)):
    for j in range (len(arr[i])):
        if arr[i][j] == 1:
            cnt+=1
print(cnt)