'''
Contains Duplicate
'''

# def containsDuplicate(self, nums: List[int]) -> bool:

#         # hash={}

#         # for num in nums:
#         #     if num in hash:
#         #         return True
#         #     else:
#         #         hash[num]=1
        
#         # return False

#         # nums=sorted(nums)

#         # for i in range(1,len(nums)):
#         #     if nums[i]==nums[i-1]:
#         #         return True
        
#         # return False


'''
isAnagram
'''

#  def isAnagram(self, s: str, t: str) -> bool:

#         if len(s)!=len(t):
#             return False

#         # s=sorted(s)
#         # t=sorted(t)

#         # if s==t:
#         #     return True
#         # return False


#         counter=[0 for i in range(26)]

#         for i in range(len(s)):
#             counter[ord(s[i])-ord('a')]+=1
#             counter[ord(t[i])-ord('a')]-=1
        
#         for count in counter:
#             if count!=0:
#                 return False
#         return True

'''
Two Sum
'''

# def twoSum(self, nums: List[int], target: int) -> List[int]:

#         hash={}

#         for i in range(len(nums)):
#             if nums[i] in hash:
#                 return [hash[nums[i]],i]
#             else:
#                 hash[target-nums[i]]=i

'''
Permutation in a string
'''

#  def checkInclusion(self, s1: str, s2: str) -> bool:
        
#         if len(s1)>len(s2):return False

#         s1_chars=[0 for i in range(26)]
#         s2_chars=[0 for i in range(26)]

#         for i in range(len(s1)):
#             s1_chars[ord(s1[i])-ord('a')]+=1
#             s2_chars[ord(s2[i])-ord('a')]+=1

#         match_count=0

#         for i in range(26):
#             if s1_chars[i]==s2_chars[i]:
#                 match_count+=1

#         start=0
#         for end in range(len(s1),len(s2)):
#             if match_count==26: return True
            
#             idx=ord(s2[end])-ord('a')
#             s2_chars[idx]+=1
#             if s1_chars[idx]==s2_chars[idx]:
#                 match_count+=1
#             elif s2_chars[idx]-1==s1_chars[idx]:
#                 match_count-=1
            
#             idx=ord(s2[start])-ord('a')
#             s2_chars[idx]-=1
#             if s1_chars[idx]==s2_chars[idx]:
#                 match_count+=1
#             elif s2_chars[idx]+1==s1_chars[idx]:
#                 match_count-=1
#             start+=1

#         return match_count==26 


'''
49. Group Anagrams- 
'''

# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         grp=[]
#         hash_map={}
#         count=0
        
#         for word in strs:
#             word_sorted=''.join(sorted(word))
            
#             if word_sorted in hash_map:
#                 grp[hash_map[word_sorted]].append(word)
#             else:
#                 grp.append([word])
#                 hash_map[word_sorted]=count
#                 count+=1
            
        
#         return grp

#------------------------------------------------------------------------------------------------

# Linked List:

'''
1. Reorder List
'''

#  def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """

#         if not head.next: return head

#         slow=head
#         fast=head

#         while(fast and fast.next):
#             prev=slow
#             slow=slow.next
#             fast=fast.next.next

#         curr=slow
#         prev.next=None
#         prev=None
       
#         while(curr):
#             nn=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nn
       
#         h=dummy=ListNode()

#         while(head and prev):
#             dummy.next=head
#             dummy,head=dummy.next,head.next
#             dummy.next=prev
#             dummy,prev=dummy.next,prev.next
        
#         return(h.next)

'''
347. Top K frequent Elements
'''
#  def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         nums_count=collections.Counter(nums)
#         max_freq=max(nums_count.values())

#         buckets=[[] for i in range(max_freq)]

#         for i in nums_count:
#             buckets[nums_count[i]-1].append(i)

#         ans=[]
#         for i in range(len(buckets)-1,-1,-1):
#             if k==0:
#                 break
#             for num in buckets[i]:
#                 ans.append(num)
#                 k-=1

#         return(ans)

'''
36. Valid Sudoku
'''

# def isValidSudoku(self, board: List[List[str]]) -> bool:

#         n=9
#         rows=[set() for i in range(n)]
#         cols=[set() for i in range(n)]
#         boxes=[set() for i in range(n)]

#         for r in range(9):
#             for c in range(9):
#                 val=board[r][c]

#                 if val=='.':
#                     continue
                
#                 if val in rows[r]:
#                     return False
                
#                 rows[r].add(val)

#                 if val in cols[c]:
#                     return False
                
#                 cols[c].add(val)

#                 box_idx=(r//3)*3+(c//3)

                
#                 if val in boxes[box_idx]:
#                     return False
                
#                 boxes[box_idx].add(val)
        
#         return True


'''
239. SLiding window max
'''

# def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

#         stack=[]
#         ans=[]
#         queue=collections.deque()

#         for i in range(len(nums)):
#             while queue and nums[i]>nums[queue[-1]]:
#                 queue.pop()

#             queue.append(i)

#             if queue[0]+k==i:
#                 queue.popleft()
            
#             if i>=k-1:
#                 ans.append(nums[queue[0]])
        
#         return ans

'''
853.  Car Fleet
'''
# def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

#         stack=[]

#         for position, speed in sorted(zip(position,speed))[::-1]:

#             distance=target-position
#             time=distance/speed
#             if not stack:
#                 stack.append(time)
#             elif time>stack[-1]:
#                 stack.append(time)
        
#         return len(stack)

########################################################
'''
543. Diameter of Binary Tree
'''

#  diameter=0
#         def dfs(root):

#             if not root:
#                 return 0

#             nonlocal diameter

#             left=dfs(root.left)
#             right=dfs(root.right)

#             diameter=max(diameter,right+left)
            
#             return max(right,left)+1

#         dfs(root)
#         return diameter

'''
110. Balanced Binary Tree
'''

#  def isBalanced(self, root: Optional[TreeNode]) -> (bool,int):

#         def bottom_up(root):
#             if not root:
#                 return True,0

#             # def depth(root):
#             #     if not root:
#             #         return 0
#             #     left=depth(root.left)
#             #     right=depth(root.right)
#             #     return 1+max(left,right)
            
#             left_balance,left_height=bottom_up(root.left)

#             if not left_balance:
#                 return False,0
#             right_balance,right_height=bottom_up(root.right)

#             if not right_balance:
#                 return False,0

#             return abs(left_height-right_height)<=1, 1+max(left_height,right_height)
        
        
#         return(bottom_up(root)[0])