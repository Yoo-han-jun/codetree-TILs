a = list(map(int, input().split()))

# Please write your code here.

print(max(a[2]-a[1], a[1]-a[0])-1)