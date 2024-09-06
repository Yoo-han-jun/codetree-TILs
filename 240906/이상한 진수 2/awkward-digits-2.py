n = list(map(int, input()))

if 0 in n :
    n[n.index(0)] = 1
elif 0 not in n:
    n[len(n)-1] = 0
sum_val = 0
for i in range (len(n)):
    sum_val = (sum_val+n[i])*2
print(sum_val//2)