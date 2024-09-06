n = list(map(int, input()))
n[n.index(0)] = 1
sum_val = 0
for i in range (len(n)):
    sum_val = (sum_val+n[i])*2
print(sum_val//2)