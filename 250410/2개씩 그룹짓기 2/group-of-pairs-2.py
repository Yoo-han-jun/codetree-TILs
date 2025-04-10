n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()
arr1 = arr[0:n]
arr2 = arr[n:2*n]
cnt = 100000000000000
for i in range (n):
    cnt2 = arr2[i]-arr1[i]
    cnt = min(cnt2, cnt)
print(cnt)