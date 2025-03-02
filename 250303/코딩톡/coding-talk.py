n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.

l = {idx: 0 for idx in range (n)}
for i in range (p-1, m):
    l[ord(c[i])-65] +=1

for k, v in l.items():
    if v==0:
        print(chr(k+65),end=" ")
