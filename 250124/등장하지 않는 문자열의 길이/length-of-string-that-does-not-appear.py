N = int(input())
str = input()
num = 0
# Write your code here!
for i in range (1,N+1):
    cnt = str[:i]
    ans = False
    for j in range (i, N-i+1):
        cnt2 = str[j:j+i]
        if cnt == cnt2:
            ans = True
            continue
    if ans == False:
        num =i
        break
print(num)
