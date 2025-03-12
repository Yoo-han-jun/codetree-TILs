n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
A_s = 0
B_s = 0
cnt= 0
arr = [0, 0, 1]
for i in range (n):
    if c[i]=="A":
        A_s+=s[i]
    else:
        B_s+=s[i]
    arr2 = arr.copy()
    if A_s>B_s:
        arr[0] = 1
        arr[1] = 0
        arr[2] = 0
    if A_s<B_s:
        arr[0] = 0
        arr[1] = 1
        arr[2] = 0
    if A_s==B_s:
        arr[0] = 0
        arr[1] = 0
        arr[2] = 1
    if arr2!=arr:
        cnt+=1
print(cnt)

        
