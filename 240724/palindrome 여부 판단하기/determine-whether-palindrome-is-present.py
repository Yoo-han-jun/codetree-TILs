def p(st):
    dt =""
    for ele in st[::-1]:
        dt+=ele
    if dt == st:
        print("Yes")
    else:
        print("No")
sr = input()
p(sr)