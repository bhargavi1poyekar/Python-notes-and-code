# '''
# 1047. Remove All Adjacent Duplicates In String
# '''
# # def removeDuplicates(self, s: str) -> str:

# #         stack=[]

# #         for i in s:
# #             if not stack:
# #                 stack.append(i)
# #             else:
# #                 if stack[-1]==i:
# #                     stack.pop()
# #                 else:
# #                     stack.append(i)
        
# #         return(''.join(stack))

# '''
# 844. Backspace String Compare
# '''

# # def backspaceCompare(self, s: str, t: str) -> bool:

# #         stack1=[]
# #         stack2=[]
# #         for i in s:
# #             # print(stack1)
# #             if i=='#' and stack1:
# #                 stack1.pop()
# #             elif i!='#':
# #                 stack1.append(i)

        
# #         for i in t:
# #             # print(stack2)
# #             if i=='#' and stack2:
# #                 stack2.pop()
# #             elif i!='#':
# #                 stack2.append(i)
        
# #         return stack1==stack2
        

# '''
# 1566. Make The String Great
# '''

# # def makeGood(self, s: str) -> str:
# #         stack=[]

# #         for i in s:
# #             if stack and i!=stack[-1] and i.lower()==stack[-1].lower():
# #                 stack.pop()
# #             else:
# #                 stack.append(i)
        
# #         return(''.join(stack))

# '''
# 739.Daily Temperatures
# '''

# # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

# #         stack=[]
# #         answer=[0 for i in range(len(temperatures))]

# #         for i in range(len(temperatures)):
# #             while stack and temperatures[i]>temperatures[stack[-1]]:
# #                 j=stack.pop()
# #                 answer[j]=i-j
            
# #             stack.append(i)
        
# #         return answer

# '''
# 496. Next Greater Element I
# '''
# def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

#         stack=[]
#         hash_pair={}
#         for i in range(len(nums2)):
#             while stack and nums2[i]>stack[-1]:
#                 hash_pair[stack.pop()]=nums2[i]
#             stack.append(nums2[i])

#         while stack:
#             hash_pair[stack.pop()]=-1
        

#         ans=[]
#         for i in nums1:
#             if i in hash_pair:
#                 ans.append(hash_pair[i])
#             else:
#                 ans.append(-1)
        
#         return ans

# '''
# 901. Online stock pan
# '''

# class StockSpanner:

#     def __init__(self):
#         self.stack=[]


#     def next(self, price: int) -> int:
#         ans=1

#         while self.stack and self.stack[-1][0]<=price:
#             ans+=self.stack.pop()[1]
        
#         self.stack.append([price,ans])
#         return ans


#         return count
        
# '''
# 2390. Remove stars from a string.
# '''

# def removeStars(self, s: str) -> str:

#         stack=[]

#         for i in s:
#             if stack and i=='*':
#                 stack.pop()
#             else:
#                 stack.append(i)

#         return(''.join(stack))

# '''
# 232. Implement queue using stacks.
# '''

# class MyQueue:

#     def __init__(self):
#         self.stack=[]
#         self.stack2=[]

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         if not self.stack2:
#             while(self.stack):
#                 self.stack2.append(self.stack.pop())
        
#         return self.stack2.pop()

#     def peek(self) -> int:
#         if self.stack2:
#             return self.stack2[-1]
#         return self.stack[0]

#     def empty(self) -> bool:
#         # print(self.stack)
#         return not self.stack and not self.stack2
    
# '''
# 2434. Using a Robot to Print the Lexicographically Smallest String
# '''
#  def robotWithString(self, s: str) -> str:

#         count=Counter(s)
#         t_stack,ans=[],[]

#         for ch in s:
#             t_stack.append(ch)

#             if count[ch]==1:
#                 del count[ch]
#             else:
#                 count[ch]-=1
            
#             while count and t_stack and min(count)>=t_stack[-1]:
#                 ans.append(t_stack.pop())
        
#         while(t_stack):
#             ans.append(t_stack.pop())
        
#         return ''.join(ans)

'''
946. Validate Stack Sequences:
# '''
# def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

#         stack=[]
#         pop_idx=0
#         for i in pushed:
#             stack.append(i)
#             while(stack and stack[-1]==popped[pop_idx]):
#                 stack.pop()
#                 pop_idx+=1
            
#         return not stack

'''
735. Asteroid Collision
'''

# def asteroidCollision(self, asteroids: List[int]) -> List[int]:

#         stack=[]
        
#         for i in range(len(asteroids)):
#             flag=1
#             while stack and (stack[-1]>0 and asteroids[i]<0):
#                 if abs(asteroids[i])>abs(stack[-1]):
#                     stack.pop()
#                     continue
#                 elif abs(asteroids[i])==abs(stack[-1]):
#                     stack.pop()
#                     flag=0

#                 flag=0
#                 break
            
#             if flag:
#                 stack.append(asteroids[i])

#         return stack
            
# '''
# 1944. 
# '''

# # def canSeePersonsCount(self, heights: List[int]) -> List[int]:

# #         stack=[]
# #         ans=[0 for i in range(len(heights))]
# #         for ht in range(len(heights)-1,-1,-1):
# #             count=0
# #             while stack and stack[-1]<heights[ht]:
# #                 # print(stack)
# #                 count+=1
# #                 stack.pop()

# #             if stack:
# #                 ans[ht]=count+1
# #             else:
# #                 ans[ht]=count
# #             stack.append(heights[ht])
        
# #         return ans

'''
2104/ SUm of subarray ranges.
'''

# def subArrayRanges(self, nums: List[int]) -> int:

#         stack=[-1]
#         subsum=0
#         for right in range(len(nums)+1):

#             while stack[-1]!=-1 and (right==len(nums) or nums[stack[-1]]>=nums[right]):

#                 target=stack.pop()
#                 left=stack[-1]
#                 numsub=(target-left)*(right-target)
#                 subsum-=numsub*nums[target]
            
#             stack.append(right)
        
#         stack.clear()
#         stack=[-1]

#         for right in range(len(nums)+1):

#             while stack[-1]!=-1 and (right==len(nums) or nums[stack[-1]]<=nums[right]):

#                 target=stack.pop()
#                 left=stack[-1]
#                 numsub=(target-left)*(right-target)
#                 subsum+=numsub*nums[target]
            
#             stack.append(right)
        
#         return subsum