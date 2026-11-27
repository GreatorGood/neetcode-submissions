import heapq

class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []


    def addNum(self, num: int) -> None:
        if len(self.heap1) == len(self.heap2):
            if self.heap2:
                if num <= self.heap2[0]:
                    heapq.heappush(self.heap1,-num)
                else:
                    heapq.heappush(self.heap1,-heapq.heappop(self.heap2))
                    heapq.heappush(self.heap2,num)
            else:
                heapq.heappush(self.heap1,-num)
        else:
            if num >= -self.heap1[0]:
                heapq.heappush(self.heap2,num)
            else:
                heapq.heappush(self.heap2,-heapq.heappop(self.heap1))
                heapq.heappush(self.heap1,-num)

        
        



    def findMedian(self) -> float:
        
        if len(self.heap1) == len(self.heap2):

            return (-self.heap1[0] + self.heap2[0])/2
        else:
            return -self.heap1[0]
        