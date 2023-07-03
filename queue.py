'''
933. Number of Recent Calls
'''
class RecentCounter:

    def __init__(self):
        self.queue=collections.deque()

    def ping(self, t: int) -> int:

        while self.queue and self.queue[0]<t-3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)


'''
346. Moving Avg from data stream
'''

class MovingAverage:

    def __init__(self, size: int):
        self.queue=collections.deque()
        self.size=size
        self.sum=0
        self.count=0

    def next(self, val: int) -> float:
        self.count+=1

        if self.count>self.size:
            self.sum-=self.queue[0]
            self.queue.popleft()
            self.count-=1
        
        self.sum+=val
        self.queue.append(val)

        return self.sum/self.count

        