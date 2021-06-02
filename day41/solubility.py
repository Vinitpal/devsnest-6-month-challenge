
# question from codechef long challenge
t = int(input())
for _ in range(t):
    x, a, b = list(map(int, input().split()))

    water = 0

    water = a + (100-x)*b
    print(water*10)
