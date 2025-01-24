N = int(input())
str = input()
num = 1010101
# Write your code here!
for i in range (1,N+1):
    answer = True
    for k in range (0, N-i+1):
        if answer == False:
            continue
        cnt = str[k:k+i]
        for j in range (k+1, N-i+1):
          cnt2 = str[j:j+i]
          if cnt == cnt2:
            answer = False
            continue
    if answer == True:
        num = min(num, i)
print(num)
