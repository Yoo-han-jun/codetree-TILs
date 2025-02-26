a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

def cross(a, b, c, d):
    if b<c or d<a:
        return abs(a-b)+abs(c-d)
    else:
        return abs(max(a,b,c,d) - min(a,b,c,d))

print(cross(a,b,c,d))