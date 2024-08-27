n = int(input())
nx, ny = 0, 0
for _ in range (n):
    a, b = tuple(input().split())
    b = int(b)
    arr = ["E", "W", "S", "N"]
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    nx, ny = nx+ b*dx[arr.index(a)], ny+ b*dy[arr.index(a)]
print(nx, ny)