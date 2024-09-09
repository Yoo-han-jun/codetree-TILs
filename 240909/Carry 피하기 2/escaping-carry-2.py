n = int(input())
a = []
for _ in range (n):
    b = int(input())
    a.append(b)

sum_val = -1
for i in range (n):
    for j in range (i+1, n):
        for k in range (j+1, n):
            cnt_val = 0
            x, y, z = a[i], a[j], a[k]
            for _ in range (4):
                if (x%10 + y%10 + z%10) >=10:
                    cnt_val = -1
                x = x//10 
                y = y//10
                z = z//10
            if cnt_val!=-1:
                cnt_val = a[i]+a[j]+a[k]
            sum_val = max(sum_val, cnt_val)
print(sum_val)