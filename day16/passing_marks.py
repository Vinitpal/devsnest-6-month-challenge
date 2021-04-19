# cook your dish here
t = int(input())
for i in range(t):
    amin, bmin, cmin, tmin, a, b, c = list(map(int, input().split()))
    total = a + b + c
    
    if a < amin or b < bmin or c < cmin:
        print("NO")    
    if a >= amin and b >= bmin and c >= cmin and total < tmin:
        print("NO")
    if a >= amin and b >= bmin and c >= cmin and total >= tmin:
        print("YES")