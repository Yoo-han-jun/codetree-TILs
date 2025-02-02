N = int(input())
seat = input()

# Write your code here!
max_dis = 0
arr2 = []    
for i,ele in enumerate (seat):
    if int(ele) == 1:
        arr2.append(i)
    
for i in range (N):
    for j in range (i+1,N):
        if i in arr2 or j in arr2:
            continue
        arr3 = []
        for ele in arr2:
            arr3.append(ele)
        arr3.append(i)
        arr3.append(j)
        arr3.sort()
        arr4 = []
        for k in range (len(arr3)-1):
            dis = arr3[k+1]-arr3[k]
            arr4.append(dis)
        max_dis = max(max_dis, min(arr4))
print(max_dis)