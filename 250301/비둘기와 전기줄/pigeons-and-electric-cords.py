N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Write your code here!
arr = []
cnt = 0
l = [0 for _ in range (11)]
for i in range (N):
    if pigeon[i] not in arr:
        arr.append(pigeon[i])
        l[pigeon[i]] = position[i]
    if pigeon[i] in arr:
        if position[i]!=l[pigeon[i]]:
            cnt+=1
            l[pigeon[i]] = position[i]
print(cnt)