n = int(input())
blocks = [int(input()) for _ in range(n)]
cnt = 0
# Please write your code here.
arr = int(sum(blocks)//n)
for i in range (n):
    cnt+=abs(arr-blocks[i])

print(cnt//2)
    