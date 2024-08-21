n = int(input())
arr = [0]*200001
cnt = 100000
for _ in range (n):
    a, b = tuple(input().split())
    a = int (a)
    if b == "R":
        for i in range(cnt, cnt+a): # 뒤집0, 1, 2, 3커서3
            arr[i] = 1
        cnt = cnt+a-1
    elif b=="L":
        for i in range(cnt, cnt-a,-1): # 뒤집3, 2, 1, 0, -1 커서-1
            arr[i] = -1
        cnt = cnt-a+1
print(arr.count(-1), arr.count(1))