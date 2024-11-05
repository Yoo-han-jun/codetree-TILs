T, a, b = map(int,input().split())
arr = [0 for _ in range (1001)]
sarr = []
narr= []
for _ in range(T):
    t, w = input().split()
    w = int(w)
    if t=="S" :
        sarr.append(w)
    else:
        narr.append(w)
arrt = []
for i in range (a, b+1):
    s_min = 2000
    j_min = 2000
    for j in range (len(sarr)):
        cnt_s = abs(sarr[j]-i)
        s_min = min(cnt_s, s_min)
    for k in range (len(narr)):
        cnt_k = abs(narr[k]-i)
        j_min = min(cnt_k, j_min)
    if s_min<=j_min:
        arrt.append(i)
print(len(arrt))