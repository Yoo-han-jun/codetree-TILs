max_n =0
min_n =0
for _ in range (3):
    n = input()
    if max_n<len(n):
        max_n = len(n)
    elif min_n>len(n):
        min_n = len(n)
    if min_n == 0:
        min_n = len(n)
print(max_n - min_n)