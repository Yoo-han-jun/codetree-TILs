n = int(input())
arr = list(input().split())

# Please write your code here.
arr2 = []
for i in range (n):
    arr2.append(ord(arr[i])-65)
cnt = 0
for i in range (n):
    r = arr2.index(i)
    arr2.insert(i, i)
    arr2.pop(r+1)
    cnt+=r-i
print(cnt)