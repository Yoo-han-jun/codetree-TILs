x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Write your code here!

def intersect(x1, y1, x2, y2, a1, b1, a2, b2):
    if x2>=a1 and x2<=a2 and y1>=b1 and y1<=b2:
        print("overlapping")
    else:
        print("nonoverlapping")

intersect(x1,y1,x2,y2,a1,b1,a2,b2)
        