# # import collections
# # '''
# # 933. Number of Recent Calls
# # '''
# # class RecentCounter:

# #     def __init__(self):
# #         self.queue=collections.deque()

# #     def ping(self, t: int) -> int:

# #         while self.queue and self.queue[0]<t-3000:
# #             self.queue.popleft()
        
# #         self.queue.append(t)
# #         return len(self.queue)


# # '''
# # 346. Moving Avg from data stream
# # '''

# # class MovingAverage:

# #     def __init__(self, size: int):
# #         self.queue=collections.deque()
# #         self.size=size
# #         self.sum=0
# #         self.count=0

# #     def next(self, val: int) -> float:
# #         self.count+=1

# #         if self.count>self.size:
# #             self.sum-=self.queue[0]
# #             self.queue.popleft()
# #             self.count-=1
        
# #         self.sum+=val
# #         self.queue.append(val)

# #         return self.sum/self.count

# # '''
# # 1438. Longest Continuous Subarray With Absolute 
# # '''
# #  def longestSubarray(self, nums: List[int], limit: int) -> int:
# #         ascend=deque()
# #         descend=deque()

# #         left=ans=0

# #         for right in range(len(nums)):

# #             while ascend and ascend[-1]>nums[right]:
# #                 ascend.pop()
# #             while descend and descend[-1]<nums[right]:
# #                 descend.pop()

# #             ascend.append(nums[right]) 
# #             descend.append(nums[right])

# #             while descend[0]-ascend[0]>limit:
# #                 if descend[0]==nums[left]:
# #                     descend.popleft()
# #                 elif ascend[0]==nums[left]:
# #                     ascend.popleft()

# #                 left+=1

# #             ans=max(ans,right-left+1) 
        
# #         return ans
        
# '''
# 225. Implement stack using queues
# '''
# class MyStack:

#     def __init__(self):
#         self.queue=deque()
#         self.queue2=deque()

#     def push(self, x: int) -> None:
#         top=x
#         self.queue.append(x)
        
#     def pop(self) -> int:
#         while len(self.queue)>1:
#             top=self.queue.popleft()
#             self.queue2.append(top)
        
#         top=self.queue.popleft()
#         self.queue2,self.queue=self.queue,self.queue2
#         return top

#     def top(self) -> int:
#         return self.queue[-1]

#     def empty(self) -> bool:
#         return not self.queue and not self.queue2
    
# '''
# 1475. Final Prices With a Special Discount in a Shop
# '''

# def finalPrices(self, prices: List[int]) -> List[int]:

#         stack=[]
#         ans=prices

#         for i in range(len(prices)):
#             while(stack and prices[stack[-1]]>=prices[i]):
#                 index=stack.pop()
#                 ans[index]=prices[index]-prices[i]
            
#             stack.append(i)
        
#         return(ans)


# '''
# 1673. 
# '''

# #  def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

# #         queue=deque()

# #         count=len(nums)-k

# #         for num in nums:
# #             # print(queue)
# #             while(queue and queue[-1]>num and count):
# #                 queue.pop()
# #                 count-=1
            
# #             queue.append(num)
        
# #         return(list(queue)[:k])

  
# '''
# 649. DOTA2 Senate
# '''

# def predictPartyVictory(self, senate: str) -> str:

#     rq,dq=deque(),deque()

#     for i in range(len(senate)):
#         if senate[i]=='R':
#             rq.append(i)
#         else:
#             dq.append(i)
#     ptr=0
#     while rq and dq:
#         if senate[ptr]=='R' and ptr in rq:
#             dq.popleft()
#             rq.append(rq.popleft())
#         elif senate[ptr]=='D' and ptr in dq:
#             rq.popleft()
#             dq.append(dq.popleft())
#         ptr=(ptr+1)%len(senate)
    
#     return 'Radiant' if rq else 'Dire'

# '''
# 2398. Maximum Number of Robots Within Budget
# '''

# #  def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

# #         left=0
# #         max_charge=deque()
# #         sum_run=0
# #         max_length=0

# #         for right in range(len(chargeTimes)):
            
# #             while max_charge and max_charge[-1]<chargeTimes[right]:
# #                 max_charge.pop()
                
# #             max_charge.append(chargeTimes[right])

# #             sum_run+=runningCosts[right]
            
# #             while(max_charge and (max_charge[0]+(right-left+1)*sum_run)>budget):
# #                 sum_run-=runningCosts[left]
# #                 if max_charge[0]==chargeTimes[left]:
# #                     max_charge.popleft()
# #                 left+=1
            
# #             max_length=max(max_length,right-left+1)
        
# #         return max_length
                
