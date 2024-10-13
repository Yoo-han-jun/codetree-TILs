n = int(input())
arr = [tuple(map(int,input().split())) for _ in range (n)]
arr2 = [0 for _ in range (101)]
cnt = 0
union = True
for i in range(n):
    for j in range (i+1, n):
        for k in range (j+1, n):
            for l in range(n):
                if l==j or l==k or l==i:
                    continue
                pointx1, pointx2 = arr[l]
                for m in range (pointx1, pointx2+1):
                    arr2[m]+=1
            for o in range (101):
                if arr2[o]>=2:
                    union = False
            if union == True:
                cnt+=1
                arr2 = [0 for _ in range (101)]
            else:
                union = True
                arr2 = [0 for _ in range (101)]
print(cnt)