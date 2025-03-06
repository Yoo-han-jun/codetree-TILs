pos = list(map(int, input().split()))
cnt = 0
cnt2 = 0
# Please write your code here.
for i in range (3):
    for j in range(i+1,3):
        if abs(pos[i]-pos[j])==1:
            cnt+=1
        elif abs(pos[i]-pos[j])==2:
            cnt2+=1

if cnt==2:
    print(0)
elif cnt2>=1:
    print(1)
else:
    print(2)