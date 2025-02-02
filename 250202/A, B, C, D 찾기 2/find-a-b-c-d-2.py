nums = list(map(int, input().split()))
nums.sort()
answer = False
# Write your code here!
for i in range (1, 41):
    for j in range (1,41):
        for k in range (1, 41):
            for l in range (1, 41):
                arr = [i, j, k, l, i+j, j+k, k+l, l+i, i+k, j+l, i+j+k, i+j+l, i+l+k, j+k+l, i+j+k+l]
                arr.sort()
                if arr == nums:
                    print(i, j, k, l)
                    exit(0)