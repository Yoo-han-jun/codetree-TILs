inp = [input() for _ in range(3)]
cnt_val = 0
arr=list()
for i in range (3):
    inp2 = inp[0][i]+inp[1][i]+inp[2][i]
    arr.append(inp2)
arr.append(inp[0][0]+inp[1][1]+inp[2][2])
arr.append(inp[2][0]+inp[1][1]+inp[0][2])
# Write your code here!

inp = inp+arr
for i in range (8):
    k = inp[i]
    k_list = []
    for j in range (3):
        k_list.append(int(k[j]))
    k_list_set = set(k_list)
    if len(k_list_set)!=2:
        continue
    for l in range (1, 10):
        for m in range (1,10):
            cnt = 0
            for n in range (3):
                if k_list[n]==l or k_list[n]==m:
                    cnt+=1
            if cnt==3:
                cnt_val+=1
print(cnt_val//2)