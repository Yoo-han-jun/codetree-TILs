n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Write your code here!
answer = False
# y가 모두 같은 경우
for i in range (11):
    for j in range (i,11):
        for k in range (j,11):
            cnt = 0
            for l in range (n):
                if i == y[l] or j == y[l] or k== y[l]:
                    cnt +=1
            if cnt == n:
                answer = True

# x = 2 y = 1 로 될 경우
for i in range (11):
    for j in range (i,11):
        for k in range (11):
            cnt = 0
            cnt1 = 0
            cnt2 = 0
            for l in range (n):
                if i == x[l] or j == x[l]:
                    cnt1 +=1
                if k== y[l]:
                    cnt1 +=1
                if i == x[l] and k == y[l]:
                    cnt2 -=1
                if j == x[l] and k == y[l]:
                    cnt2 -=1
            cnt = cnt1+cnt2
            if cnt == n:
                answer = True
# x = 1 y = 2
for i in range (11):
    for j in range (i,11):
        for k in range (11):
            cnt = 0
            for l in range (n):
                if i == y[l] or j == y[l]:
                    cnt +=1
                if k == x[l]:
                    cnt+=1
                if i == y[l] and k== x[l]:
                    cnt -=1
                if j == y[l] and k== x[l]:
                    cnt -=1
            if cnt == n:
                answer = True
# x = 3
for i in range (11):
    for j in range (i,11):
        for k in range (j,11):
            cnt = 0
            for l in range (n):
                if i == x[l] or j == x[l] or k== x[l]:
                    cnt +=1
            if cnt == n:
                answer = True

if answer:
    print(1)
else:
    print(0)