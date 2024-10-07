n = int(input())
arr = []
for _ in range (n):
    a, b= tuple(input().split())
    arr.append((a,b))
min_val = 100000000
for i in range(n):
    max_x = 1
    min_x = 400001
    max_y = 1
    min_y = 400001
    for j in range(n):
        if i==j:
            continue
        else:
            max_x = max(max_x, int(arr[j][0]))
            min_x = min(min_x, int(arr[j][0]))
            max_y = max(max_y, int(arr[j][1]))
            min_y = min(min_y, int(arr[j][1]))
    square = (max_x-min_x)*(max_y-min_y)
    min_val = min(min_val, square)
print(min_val)