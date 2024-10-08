n = int(input())
arr = []
max_val = 0
for i in range (n):
    a, b = tuple(map(int, input().split()))
    arr.append ((a, b))
for i in range (n):
    for j in range (n):
        for k in range(n):
            if i==j or j==k or k==i:
                continue
            if (arr[i][0] == arr[j][0] and arr[j][1] == arr[k][1]) or (arr[k][0] == arr[j][0] and arr[i][1] == arr[k][1]) or (arr[i][0] == arr[j][0] and arr[j][1] == arr[k][1]):
                z = abs(arr[i][0]*arr[j][1]+arr[j][0]*arr[k][1]+arr[k][0]*arr[i][1] - arr[j][0]*arr[i][1]-arr[k][0]*arr[j][1]-arr[i][0]*arr[k][1])
                max_val = max(z, max_val)
print(max_val)