n = tuple(input())
cnt = 0
for i in range (len(n)):
    if n[i] =="(" and n[i+1] =="(":
        for k in range (i+2, len(n)-1):
            if n[k] ==")" and n[k+1] ==")":
                cnt+=1
print(cnt)