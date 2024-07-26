def z(a):
    b = []
    cnt= 0
    for ele in a:
        if ele not in b:
            b.append(ele)
    if len(b)>=2:
        return True
    else:
        return False    
s = input()
if z(s):
    print("Yes")
else:
    print("No")