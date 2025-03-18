n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
def get_score(a1, a2, a3):
    if a1==a2==a3:
        return 1
    if a1==a2 and a1<a3:
        return 2
    if a1==a2 and a1>a3:
        return 3
    if a2==a3 and a2>a1:
        return 4
    if a2==a3 and a2<a1:
        return 5
    if a1==a3 and a3<a2:
        return 6
    if a1==a3 and a3>a2:
        return 7
    if a1!=a2 and a2!=a3 and a3!=a2:
        if max(a1, a2, a3)==a1:
            return 5
        if max(a1, a2, a3)==a2:
            return 6
        if max(a1, a2, a3)==a3:
            return 2
arr = [0, 0, 0]
state = 1
state_arr = []
cnt = 0
for i in range (n):
    state = get_score(arr[0], arr[1], arr[2])
    if c[i] =="A":
        arr[0]+=s[i]
    if c[i]=="B":
        arr[1]+=s[i]
    if c[i]=="C":
        arr[2]+=s[i]
    if state != get_score(arr[0], arr[1], arr[2]):
        cnt+=1

print(cnt)