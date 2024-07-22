arr = ["apple", "banana", "grape", "blueberry", "orange"]
n = input()
s = 0
for i in range (1,5):
    cnt = 0
    for ele in arr[i][2:4]:
        if ele==n:
            cnt+=1
    if cnt>0:
        s+=1
        print(arr[i])
print(s)