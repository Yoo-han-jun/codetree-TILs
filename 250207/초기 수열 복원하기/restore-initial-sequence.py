n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
for i in range (1,n+1):
    arr2 = []
    arr2.append(i)
    for j in range (0, n-1):
        s = arr[j]-arr2[j]
        if s in arr2 or s>n:
            break
        arr2.append(arr[j]-arr2[j])
    if len(arr2)==n:
        break
print(*arr2)