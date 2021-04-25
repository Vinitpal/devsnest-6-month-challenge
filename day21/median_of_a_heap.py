import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.first_half = []  #maxheap
        self.second_half = []  #minheap
       
    
    def addNum(self, num: int) -> None:
        if not self.first_half:
            heapq.heappush(self.first_half, -num)
            return 
        
        if(num <= -self.first_half[0]):
            heapq.heappush(self.first_half, -num)
            
        else:
            heapq.heappush(self.second_half, num)
         
        #balance part 
        
        if(len(self.first_half) > len(self.second_half)+1 ):
            heapq.heappush(self.second_half, -heapq.heappop(self.first_half))
            
        elif(len(self.second_half) > len(self.first_half)+1 ):
            heapq.heappush(self.first_half, -heapq.heappop(self.second_half))
    
        
        
            

    def findMedian(self) -> float:
        if(len(self.first_half) == len(self.second_half)):
            return ( -float(self.first_half[0])  + float(self.second_half[0]) ) / 2.0
        
        if(len(self.first_half) > len(self.second_half)):
            return - float(self.first_half[0])
            
            
        else:
            return  float(self.second_half[0])

# import heapq

# class MedianFinder:

#     def __init__(self):
#         self.maxH = []
#         self.minH = []
        

#     def addNum(self, num: int) -> None:
#         if len(self.maxH) == len(self.minH):
#             heappush(self.minH, -heappushpop(self.maxH, -num))
#         else:
#             heappush(self.maxH, -heappushpop(self.minH, num))

#     def findMedian(self) -> float:
#         if len(self.maxH) == len(self.minH):
#             return float(self.minH[0] - self.maxH[0]) / 2.0
#         else:
#             return float(self.minH[0])
