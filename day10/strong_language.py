# cook your dish here
T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    S = str(input())

    flag = "No" 
    i = 0
    j = 0
    for x in range(N):
        if S[x] != "*":
            i = 0
        if S[x] == "*":
            i += 1
            j = max(i, j)
        if j == K:
            flag = "Yes"
            break
            
    print(flag)
