n, k = map(int,input().split())
arr = [0]*10000
brr = [0]*10000
for i in range (n):
    a, b = input().split()
    arr[int(a)] = 1
    brr[int(a)] = b
sum_val = 0
for i in range (10000-k):
    cnt = 0
    for j in range (i, i+k+1):
        if brr[j] == "G":
            cnt +=1
        if brr[j] == "H":
            cnt+=2
        sum_val = max(sum_val, cnt)
print(sum_val)