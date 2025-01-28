n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)
arr = []
# Write your code here!
for i in range (10000):
    ans = False
    k = i
    for j in range (n):
        k = 2*k
        if a[j]>k or b[j]<k:
            ans = True
    if ans == False:
        arr.append(i)
print(min(arr))

            
