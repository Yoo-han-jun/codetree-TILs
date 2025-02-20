n, m = map(int, input().split())
a = list(map(int, input().split()))
max_num = 100000
# Write your code here!

for i in range (max(a), max_num):
    max_cnt = 0
    s = 1
    cnt = 0
    for j in range (len(a)):
        if a[j]>i:
            break
        if cnt+a[j]<=i:
            cnt+=a[j]
            continue
        elif cnt+a[j] >i:
            s +=1
            cnt = a[j]
        
    if s == m:
        print(i)
        break