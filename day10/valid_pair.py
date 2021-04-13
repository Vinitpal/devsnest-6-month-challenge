# cook your dish here
a, b, c = list(map(int, input().split()))

if a == b or b == c or c == a:
    print("Yes")
else:
    print("No")