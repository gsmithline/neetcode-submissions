import heapq

class MedianFinder:

    def __init__(self):
        self.holder = []
        heapq.heapify(self.holder)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.holder, num)

    def findMedian(self) -> float:
        self.holder = sorted(self.holder)
        middle = len(self.holder) // 2
        if len(self.holder) % 2 == 0:
            middle_less = middle - 1
            return .5 * (self.holder[middle_less] + self.holder[middle])
        else:
            return self.holder[middle]

        
        