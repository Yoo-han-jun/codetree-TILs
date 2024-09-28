n = int(input())
arr = [ 0 for _ in range (101)]
arr2 = []
for i in range (n):
    a, b = input().split()
    arr2.append(int(a))
    arr[int(a)] = b
arr2.sort()
max_val = 0
for i in range (len(arr2)):
    for j in range (i, len(arr2)):
        cnt_G = 0
        cnt_H = 0
        cnt_val = 0
        for k in range (i, j+1):
            if arr[arr2[k]] == "G":
                cnt_G+=1
            if arr[arr2[k]] == "H":
                cnt_H+=1
        if cnt_G == cnt_H:
            cnt_val = arr2[j]-arr2[i]+1
    max_val = max(max_val, cnt_val)
print(max_val)