n = int(input())
arr1 = [0]*200000
cnt = 100000
arr2 = [1]*200000
for _ in range (n):
    a, b= tuple(input().split())
    a = int(a)
    if b == "R":
        for i in range (cnt, cnt+a):
            arr1[i] = 1
            arr2[i] *=2
        cnt = cnt+a
    elif b=="L":
        for i in range (cnt-1, cnt-a-1,-1):
            arr1[i] = -1
            arr2[i] *= 3
        cnt = cnt-a
result = [i*j for i, j in zip(arr1, arr2)]
w = 0
b = 0
g = 0
for ele in result:
    if abs(ele)//36:
        g+=1
    elif ele>0:
        b+=1
    elif ele<0:
        w+=1
print(w, b, g)