n = int(input())
arr = list(map(int,input().split()))
arr.sort()
for ele in arr:
    print(ele,end=" ")
print()
arr.sort(reverse=True)
for ele in arr:
    print(ele,end=" ")