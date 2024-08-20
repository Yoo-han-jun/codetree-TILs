n = int(input())
arr1 = [0]*200
cnt = 100
arr2 = [1]*200
for _ in range (n):
    a, b= tuple(input().split())
    a = int(a)
    if b == "R":
        for i in range (cnt, cnt+a):
            arr1[i] = 1
            arr2[i] *=2
        cnt = cnt+a-1
    elif b=="L":
        for i in range (cnt, cnt-a,-1):
            arr1[i] = -1
            arr2[i] *= 3
        cnt = cnt-a+1

result = [i*j for i, j in zip(arr1, arr2)]
w = 0
b = 0
g = 0
for ele in result:
    if ele!=0 and abs(ele)%36==0:
        g+=1
    elif ele>0:
        b+=1
    elif ele<0:
        w+=1
print(w, b, g)