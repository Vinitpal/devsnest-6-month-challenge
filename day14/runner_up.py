if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
     
    a = sorted(arr)
    temp = []
    
    for i in a:
        if i not in temp:
            temp.append(i)
    
    print(temp[-2])