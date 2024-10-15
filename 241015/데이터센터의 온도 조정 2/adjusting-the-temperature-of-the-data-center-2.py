n, c, g, h = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range (n)]
def thermal(x, Ta, Tb):
    if x< Ta:
        return c
    elif x>=Ta and x<=Tb:
        return g
    elif x>Tb:
        return h
sum_val = 0
for x in range (1001):
    cnt_val = 0
    for i in range (n):
        Ta, Tb = arr[i]
        cnt_val += thermal(x, Ta, Tb)
    sum_val = max(cnt_val, sum_val)
print(sum_val)