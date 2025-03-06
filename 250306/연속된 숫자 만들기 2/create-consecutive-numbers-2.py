pos = list(map(int, input().split()))
cnt = 0
# Please write your code here.
for i in range (2):
    if abs(pos[i]-pos[i+1])==1:
        cnt+=1

print(2-cnt)