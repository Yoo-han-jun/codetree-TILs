arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()
if arr[0]+arr[1]==arr[2]:
    print(arr[0], arr[1], arr[3])
else:
    print(arr[0], arr[1], arr[2])