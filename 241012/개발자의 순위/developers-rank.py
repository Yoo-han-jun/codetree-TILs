k, n = map(int,input().split())
arr = [(tuple(map(int,input().split()))) for _ in range (k)]
arr2 = []
for i in range (1, n+1):
    for j in range (1, n+1):
        cnt = 0
        if i==j:
            continue
        else:
            for l in range (k):
                if arr[l].index(i)>arr[l].index(j):
                    cnt+=1
        if cnt ==k or cnt ==0:
            arr2.append((i, j))
print(len(arr2)//2)