#code
from heapq import heappush, heappop
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = []
    heap = []
    
    for i in range(n):
        heappush(heap, arr[i])
        if len(heap) > k:
            ans.append(heappop(heap))
    while heap:
        ans.append(heappop(heap))
    print(*ans)