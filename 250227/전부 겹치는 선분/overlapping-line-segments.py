n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Write your code here!
answer = True
for i in range (n):
    if max(x1) > x2[i] or min(x2) < x1[i]:
        answer = False

if answer:
    print("Yes")
else:
    print("No")