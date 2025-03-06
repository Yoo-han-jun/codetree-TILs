pos = list(map(int, input().split()))
cnt = 0
cnt2 = 0
# Please write your code here.
for i in range (2):
    if abs(pos[i]-pos[i+1])==1:
        cnt+=1
    elif abs(pos[i]-pos[i+1])==2:
        cnt2+=1

if cnt2>=1:
    print(1)
elif cnt==2:
    print(0)
else:
    print(2)