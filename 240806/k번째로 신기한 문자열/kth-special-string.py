a, b, c= input().split()
a =int(a)
b =int(b)
c = str(c)
arr = []
for _ in range(a):
    n = input()
    if n[0:len(c)] == c:
        arr.append(n)

arr.sort()
print(arr[b-1])