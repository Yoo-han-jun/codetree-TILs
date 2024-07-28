n = input()
m = input()
def s(n, m):
    if m in n:
        return n.index(m)
    else:
        return -1
print(s(n,m))