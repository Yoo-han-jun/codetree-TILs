n = int(input())
sequence = list(map(int, input().split()))
arr= []
# Please write your code here.

for i in range (n-1):
    if sequence[i]>sequence[i+1]:
        arr.append(i+1)
    else:
        continue
print(max(arr))