nums = list(map(int, input().split()))
nums.sort()
# Write your code here!
for i in range (3, 41):
    for j in range (3,41):
        for k in range (4, 41):
            for l in range (7, 41):
                arr = [i, j, k, l, i+j, j+k, k+l, l+i, i+k, j+l, i+j+k, i+j+l, i+l+k, j+k+l, i+j+k+l]
                arr.sort()
                if arr == nums:
                    print(i, j, k, l)
                    break