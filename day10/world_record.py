# cook your dish here
T = int(input())



for i in range(T):
    k1, k2, k3, v = list(map(float, input().split()))    

    win = 9.58
    v2 = k1*k2*k3*v 
    v3 = 100/v2
    nV = round(v3,2)


    if nV < win:
        print("Yes")
    else:
        print("No")
