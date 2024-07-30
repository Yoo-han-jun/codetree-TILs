n, m = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range (m):
    s, b = map(int, input().split())
    sum_val=0
    if s==b:
        print(arr[s-1])
    else:
        for ele in arr[s-1:b]:
            sum_val+=ele
        print(sum_val)