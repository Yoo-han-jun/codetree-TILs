n = int(input())
arr = []
min_val = 1000000000000000000000000000000000000
for i in range (n):
    a, b = tuple(input().split())
    arr.append((a, b))
for i in range (n):
    for j in range (n-1):
        if i==j:
            continue
        else:
            distance = (int(arr[j][1])-int(arr[i][1]))**2+(int(arr[j][0])-int(arr[i][0]))**2
        min_val = min(distance, min_val)
print(min_val)