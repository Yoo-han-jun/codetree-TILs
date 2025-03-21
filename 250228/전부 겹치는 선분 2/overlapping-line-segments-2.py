n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Write your code here!

answer = False
for i in range (n):
    l = {idx: 0 for idx in range(min(x1), max(x2)+1)}
    for j in range (n):
        if i==j:
            continue
        else:
            for k in range(x1[j], x2[j]+1):
                 l[k]+=1
            if n-1 in l.values():
                answer = True

if answer:
    print("Yes")
else:
    print("No")