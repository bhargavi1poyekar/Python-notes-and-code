'''
1. Merge Sorted Arrays (88):
'''
# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
    
#         while (m>0 and n>0):
#             if nums1[m-1]> nums2[n-1]:
#                 nums1[m+n-1]=nums1[m-1]
#                 m-=1 
#             else:
#                 nums1[m+n-1]=nums2[n-1]
#                 n-=1
        
#         if n>0:
#             nums1[0:n]=nums2[0:n]

'''
1. 2 ptr approach. Start both ptrs from m, n resp. and go back. Compare the values. 
Add the greater value from the end. Continue till one of them reaches start of array. 
'''

'''
2. Remove element (27)
''' 

# def removeElement(nums, val):
    
#     count=0
#     for i in range(len(nums)):
#         if nums[i]!=val:
#             nums[count]=nums[i]
#             count+=1
    
#     return (count,nums[:count])

# print(removeElement([3,2,2,3,4,4,3,2,3,5,2],2))

'''
Keep a count of valid numbers. Add new element to count index only if it is not the number to be removed.
'''

'''
3. Remove Duplicates form Sorted Array (26)
'''
# def removeDuplicates(self, nums: List[int]) -> int:

#         ptr1=0
#         ptr2=1
#         n=len(nums)

#         while(ptr2<n):
#             if  nums[ptr1]!=nums[ptr2]:
#                 ptr1+=1
#                 nums[ptr1]=nums[ptr2]
#             ptr2+=1
        
#         return ptr1+1

'''
fast and slow ptr: increment fast, till element not equal to slow ptrs element.
then increment slow ptr, and put new element at slow ptr.
'''

'''
4. Remove Duplicates from Sorted Array 2 (80)
'''

# def removeDuplicates(self, nums: List[int]) -> int:

#         ptr1=0
#         ptr2=1
#         n=len(nums)
#         count=1

#         while(ptr2<n):
#             if nums[ptr1]==nums[ptr2] and count<2:
#                 ptr1+=1
#                 nums[ptr1]=nums[ptr2]
#                 count+=1
#             elif  nums[ptr1]!=nums[ptr2]:
#                 ptr1+=1
#                 nums[ptr1]=nums[ptr2]
#                 count=1
#             ptr2+=1
        
#         return ptr1+1

'''
Keep count of same numbers, till the count is less than 2, can copy. else skip
'''

'''
5. Majority Element ()
'''
# def majorityElement(self, nums: List[int]) -> int:

#         # O(n)=> time but O(n)=>space
#         count_tab={}
#         major_cond=(len(nums)//2)+1
#         for num in nums:
#             if num in count_tab:
#                 count_tab[num]+=1
#             else:
#                 count_tab[num]=1
        
#         for item in count_tab:
#             if count_tab[item]>=major_cond:
#                 return item 

'''
6. Rotate Array (189)
'''

# def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k=k%len(nums)
#         nums=self.reverse(nums,0,len(nums)-1)
#         nums=self.reverse(nums,0,k-1)
#         nums=self.reverse(nums,k,len(nums)-1)
#         return nums

# def reverse(self,nums,start,end):
#     while(start<end):
#         temp=nums[start]
#         nums[start]=nums[end]
#         nums[end]=temp
#         start+=1
#         end-=1
#     return nums

'''
Reverse 3 times: once entire, then 0 to k-1 then k to end
'''

'''
7. Best Time to Buy and Sell Stock (121)
'''

# def maxProfit(self, prices: List[int]) -> int:

#         cheapest=prices[0]
#         max_profit=0
#         for i in range(1,len(prices)):
#             if prices[i]<cheapest:
#                 cheapest=prices[i]
#             else:
#                 profit=prices[i]-cheapest
#                 max_profit=max(profit,max_profit)
        
#         return max_profit

'''
Keep cheapest price, and max profit. If current price is less than cheapest, then it is new cheapest
Calculate new profit and compare with max.
'''


'''
8. Best Time to Buy and Sell Stock 2- 122
'''

# the most important thing here is to know that the all valleys and peaks need to be considered, hence immediate up and down prices are considered.

#  def maxProfit(self, prices: List[int]) -> int:

#         profit_max=0

#         for i in range(0,len(prices)-1):
#             if prices[i+1]>prices[i]:
#                 profit_max+=prices[i+1]-prices[i]
        
#         return profit_max

'''
Greedy approach: if next price greater than current, then add it in profit. 
'''

'''
9. Jump Game (55)
'''

# def canJump(self, nums: List[int]) -> bool:
        
#         goal=len(nums)-1

#         for curr in range(n-1,-1,-1):
#             if curr+nums[i]>=goal:
#                 goal=curr
           
#         return True if n==0 else False

'''
STart from back, and check if you can reach the end from that position, 
if possible, then our new goal is current.
'''

'''
10. Jump Game 2
'''

#  def jump(self, nums: List[int]) -> int:

#         l=0
#         r=0
#         jmp=0

#         while(r<len(nums)-1):
#             farthest=0
#             for i in range(l,r+1):
#                 farthest=max(farthest,i+nums[i])
#             l=r+1
#             r=farthest
#             jmp+=1
#         return jmp

'''
Greedy approach: Keep a window of min jump it can make, to max jump it can make.
'''

'''
11. Roman to Integer
'''

# def romanToInt(self, s: str) -> int:
#         rti={'I':1,
#         'V':5,
#         'X':10,
#         'L':50,
#         'C':100,
#         'D':500,
#         'M':1000}

#         val=0
#         i=0
#         while i<len(s)-1:
#             if rti[s[i]]<rti[s[i+1]]:
#                 val-=rti[s[i]]
#             else:
#                 val+=rti[s[i]]
#             i+=1
        
#         val+=rti[s[-1]]
#         return val

'''
Check if curr characters numeric value is less than next chars numeric value
if yes then subtract numeric value from sum
if no, then add numeric value in sum

don't forget to add last elements value. 
'''

'''
12. Length of last word
'''

# def lengthOfLastWord(self, s: str) -> int:

#         word=0
#         str_idx,end_idx=0,0
        
#         for i in range(len(s)-1,-1,-1):
#             if s[i]==' ' and word!=0:
#                 str_idx=i+1
#                 break 
#             elif s[i]!=' ' and end_idx==0:
#                 word=1
#                 end_idx=i
#         # print(str_idx,end_idx,word)
#         return end_idx-str_idx+1


'''
14. H-index
'''

# def hIndex(self, citations: List[int]) -> int

#         citations.sort(reverse=True)

#         if len(citations)==1 and citations[0]>0:
#             return 1
#         if citations[-1]>=len(citations):
#             return len(citations)
#         for i in range(len(citations)):
#             if citations[i]<i+1:
#                 return i
#         return 0


'''
15. Reverse Words 
'''

# def reverseWords(self, s: str) -> str:
        
#         flag=0
#         str2=[]
#         s=s.strip()
#         length=len(s)
#         for i in range(length):
#             if s[i] == ' ' and (i!=0 and i!=length-1):
#                 flag=1
#             elif s[i]!=' ' and flag==1:
#                 str2.append(' ')
#                 str2.append(s[i])
#                 flag=0
#             elif s[i]!=' ' and flag==0:
#                 str2.append(s[i])
        
     
#         str2=''.join(str2)
#         str2=str2.split(' ')
        
#         return ' '.join(str2[::-1])   

'''
16. Insert Delete Get Random O(1):
'''

# class RandomizedSet:

#     def __init__(self):
#         self.index={}
#         self.set=[]        

#     def insert(self, val: int) -> bool:
#         if val in self.index:
#             return False
#         self.set.append(val)
#         self.index[val]=len(self.set)-1
#         return True 

#     def remove(self, val: int) -> bool:
#         if val not in self.index: 
#             return False

#         i=self.index[val] # getindex of val
#         self.index[self.set[-1]]=i # change index of last element to i
#         self.set[i]=self.set[-1] # overwrite val with last element

#         self.index.pop(val)
#         self.set.pop()

#         return True
        

#     def getRandom(self) -> int:
#         return random.choice(self.set)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
17. Gas Station
'''

# def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

#         n=len(gas)
        

#         if sum(gas)<sum(cost):
#             return -1
           

#         start=0
#         gas_curr=0
#         for i in range(n):
#             gas_curr+=gas[i]-cost[i]
        
#             if gas_curr<0:
#                 gas_curr=0
#                 start=i+1

#         return start


# There are 4 parts to it-

# Part 1- sum of gas array>=sum of cost array---> 
# very intuitive, we should always have enough gas.

# Part 2- we are keeping a total+=gas[i]-cost[i] for each i, and whenever it is <0 we are skipping that point and moving forward, making total 0--->
#  It means we ran out of gas if we started at some point which was <= current pos of i, so now we have to find a new starting position,
# which wall be > curr pos of i.
# Now think, why will this new start lie ahead of curr pos i, not anywhere before it,  you could think, we started from point A------>B(total till +ve)------->C(total<0), as per this algo we try to find start ahead of C, what if we started from B and skipped A instead, well that won't work, You moved from A--------> B with some positive value(or 0), or else you would have stopped right at B and made total to 0. So add A improved our chances of having a positive total, so there is no point in looking for the new position start anywhere behind point C.

# Part 3- When the total stays +ve, we dn't do anything to the start point, our start pointer points to the first index when our total became positive.
# Again this is similar to the above explanation-l
# ets suppose we start from X(-ve)--->Y(-ve)--->A(+ve)---->B(+ve)---->C(+ve), where C is the end of the array, our start(which is also the ans) would be A.
# Why not B? why not C?
# It is because we moved from A to B with some +ve value or atleast 0, whereas if we started from B we would have had only the value of B so earlier point added some value to our total, so its more favorable to help us reach the ans, hence earliest point is always better.

# Part 4-- Why we just stop at point C and don t complete the cycle and check.
# It is because from Part 1 we would have already identified that if the given set of inputs will have an ans, so if we have reached to Part 3 it means we surely have an ans, and it is mentioned in the question that there is only one valid ans, so we will always choose the most favorable ans-- which is also the fundamental idea of Greedy Algorithims. There is also a mathematical proof for this, that if we got a start point given our total gas >=total cost , we will be able to reach back to that point with just enough gas. 

'''
18. Longest Common Prefix- Vertical SCanning -> O(n^2)
'''

#  def longestCommonPrefix(self, strs: List[str]) -> str:

#         if len(strs)==0:
#             return ""
        

#         word_0=strs[0]

#         for i in range(len(word_0)):
#             for word in strs[1:]:
#                 if i==len(word) or word[i]!=word_0[i]:
#                     return word_0[0:i]

#         return word_0

'''
19. Trapping Rain Water
'''
# def trap(self, height: List[int]) -> int:

#         max_left=[0 for i in range(len(height))]
#         max_right=[0 for i in range(len(height))]
#         max_l=0

#         for i in range(0,len(height)):
#             max_left[i]=max_l
#             max_l=max(height[i],max_l)

#         max_r=0
        
#         for i in range(len(height)-1,-1,-1):
#             max_right[i]=max_r
#             max_r=max(height[i],max_r)
        
        

#         for i in range(len(height)):
#             max_left[i]=min(max_left[i],max_right[i])
        
        
#         total=0
        
#         for i in range(len(height)):
#             total+=max(0,max_left[i]-height[i])

#         return total


'''
20. Find Index of first occurence of string
'''

#  def strStr(self, haystack: str, needle: str) -> int:

#         if needle not in haystack:
#             return -1

#         for i in range(len(haystack)+1-len(needle)):
#             if haystack[i:i+len(needle)]==needle:
#                 return i
#         return -1

'''
21. Zigzag Conversion
'''

# def convert(self, s: str, numRows: int) -> str:
        
#         if numRows==1:
#             return s
        
#         ans=''
#         inc=2*(numRows-1)
#         for row in range(numRows):
#             for ptr in range(row,len(s),inc):
#                 ans+=s[ptr]
#                 if row>0 and row<numRows-1 and ptr+inc-2*row<len(s):
#                     ans+=s[ptr+inc-2*row]
        
#         return ans

'''
22. isSubsequence
'''

#  def isSubsequence(self, s: str, t: str) -> bool:
#         s_ptr=len(s)-1
#         t_ptr=len(t)-1

#         if len(s)==0:
#             return True

#         while t_ptr!=-1:
#             if s[s_ptr]==t[t_ptr]:
#                  s_ptr-=1
#                  t_ptr-=1
#             else:
#                 t_ptr-=1
#         # print(s_ptr)
#         if s_ptr<0:
#             return True
#         return False

'''
23. Product of Array Itself
'''

#         ans=[1 for i in range(len(nums))]
#         curr=1 
#         for i in range(len(nums)):
#             ans[i]*=curr
#             curr*=nums[i]
        
#         curr=1

#         for i in range(len(nums)-1,-1,-1):
#             ans[i]*=curr
#             curr*=nums[i]
        
#         return ans

'''
24. Candy
'''

#  def candy(self, ratings: List[int]) -> int:
#         n=len(ratings)
#         if n==1:
#             return 1

#         left=[1 for i in range(n)]
#         right=[1 for i in range(n)]

#         for i in range(1,n):
#             if ratings[i]>ratings[i-1]:
#                 left[i]=left[i-1]+1
        
#         for j in range(n-2,-1,-1):
#             if ratings[j]>ratings[j+1]:
#                 right[j]=right[j+1]+1
            
#         count=0
#         for i in range(n):
#             count+=max(left[i],right[i])

#         return count

'''
25. Integer to Roman
'''

# def intToRoman(self, num: int) -> str:
#         roman_to_int={
#             1:'I',
#             4:'IV',
#             5:'V',
#             9:'IX',
#             10:'X',
#             40:'XL',
#             50:"L",
#             90:'XC',
#             100:'C',
#             400:'CD',
#             500:'D',
#             900:'CM',
#             1000:'M',
#         }

#         int_num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#         roman=''
#         i=0
#         while i<len(int_num):
#             # print(roman)
#             if num==0:
#                 break
#             elif num>=int_num[i]:
#                 roman+=roman_to_int[int_num[i]]
#                 num-=int_num[i]
#                 i-=1
#             i+=1
        
#         return(roman)


##############################################################################################
##############################################################################################

# Two Pointers:

'''
22. isSubsequence
'''

#  def isSubsequence(self, s: str, t: str) -> bool:
#         s_ptr=len(s)-1
#         t_ptr=len(t)-1

#         if len(s)==0:
#             return True

#         while t_ptr!=-1:
#             if s[s_ptr]==t[t_ptr]:
#                  s_ptr-=1
#                  t_ptr-=1
#             else:
#                 t_ptr-=1
#         # print(s_ptr)
#         if s_ptr<0:
#             return True
#         return False


'''
13. Valid Palindrome
'''

# def isPalindrome(self, s: str) -> bool:
        
#         s = s.lower()
#         s=re.sub(r'\W+', '', s)
#         s=s.replace('_','')
#         if len(s)<=1:
#             return True
        
#         left=0
#         right=len(s)-1

#         while(left<=right):
#             print(s[left],s[right])
#             if s[left]!=s[right]:
#                 return False
#             left+=1
#             right-=1
        
#         return True


'''
26. Two Sum II- Input Array is Sorted
'''

# def twoSum(self, numbers: List[int], target: int) -> List[int]:

#         n=len(numbers)
#         left=0
#         right=n-1

#         while(left<right):

#             if numbers[left]+numbers[right]==target:
#                 return [left+1,right+1]
#             elif target-numbers[left]<numbers[right]:
#                 right-=1
#             elif target-numbers[left]>numbers[right]:
#                 left+=1

'''
27. Container with Most Water
'''

# def maxArea(self, height: List[int]) -> int:

#         max_area=0

#         left=0
#         right=len(height)-1

#         while(left<right):
#             area=(right-left)*min(height[left],height[right])
#             max_area=max(max_area,area)

#             if height[left]>=height[right]:
#                 right-=1
#             else:
#                 left+=1
            
        
#         return max_area

'''
28. 3 Sum
'''

# def threeSum(self, nums: List[int]) -> List[List[int]]:

#         nums=sorted(nums)
#         ans=[]
#         for i in range(len(nums)):
#             if nums[i]>0:
#                 break
#             elif i!=0 and nums[i]!=nums[i-1]:
#                 ans.extend(self.twoSum(nums[i+1:],-nums[i]))
#             elif i==0:
#                 ans.extend(self.twoSum(nums[i+1:],-nums[i]))
        
#         return ans


#     def twoSum(self,nums, target):

#         left=0
#         right=len(nums)-1
#         res=[]

#         # print(nums,target)
#         while(left<right):
#             if nums[left]+nums[right]==target:
#                 res.append([-target,nums[left],nums[right]])
#                 left+=1
#                 right-=1
#                 while(left<right and nums[left]==nums[left-1]):
#                     left+=1
    
#             elif target-nums[left]<nums[right]:
#                 right-=1
#             else:
#                 left+=1
            
#         return res

###########################################################################

# Sliding Window

'''
29. Min Size SubArray Sum
'''
 
#  def minSubArrayLen(self, target: int, nums: List[int]) -> int:

#         if target in nums:
#             return 1
#         if sum(nums)<target:
#             return 0
        
#         n=len(nums)
#         min_size=n
#         left=right=0
#         subsum=nums[0]

#         while(right<n-1):
            
#             if subsum<target:
#                 right+=1
#                 subsum+=nums[right]

#             while(subsum>=target):
#                 min_size=min(min_size,right-left+1)
#                 subsum-=nums[left]
#                 left+=1
        
#         return min_size

'''
30. Longest Substring Without Repeating Characters:
'''

#  def lengthOfLongestSubstring(self, s: str) -> int:

#         hash_index={}
#         left=0
#         longest=0
#         for right in range(len(s)):
#             if s[right] in hash_index:
#                 left=max(hash_index[s[right]],left)
            
#             longest=max(longest,right-left+1)
#             hash_index[s[right]]=right+1
#         return longest

'''
76. Minimum Window Substring: 
'''

# def minWindow(self, s: str, t: str) -> str:

#         if len(t)>len(s):return ""
        

#         t_count=collections.Counter(t)
#         unique_char=len(t_count)
      
#         win_count=collections.Counter()

#         left=0  
#         sub_char=0
#         min_length=float('inf')
#         min_left=0
#         min_right=0
        
#         for right in range(len(s)):
#             win_count[s[right]]+=1

#             if win_count[s[right]]==t_count[s[right]]:
#                 sub_char+=1
            
#             while(sub_char==unique_char):
#                 if right-left+1<min_length:
#                     min_length=right-left+1
#                     min_left=left
#                     min_right=right
                
#                 if win_count[s[left]]==t_count[s[left]]:
#                     sub_char-=1
#                 win_count[s[left]]-=1
#                 left+=1
        
#         return '' if min_length==float('inf') else s[min_left:min_right+1]

##############################################################################

# Linked List

'''
141. Linked List Cycle
'''
# def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         fast=head
#         slow=head

#         while(fast and fast.next):
#             slow=slow.next
#             fast=fast.next.next
            
#             if (slow==fast):
#                 return True
            
        
#         return False

'''
92. Reverse Linked List 2
'''

# if not head:
#             return head
        
#         if left==right:
#             return head
        
#         prev=None
#         curr=head

#         # Bringing prev and curr to their positions: curr=>left and prev=left-1
#         while(left>1):
#             prev=curr
#             curr=curr.next
#             left,right=left-1,right-1 # dec left,n
        
#         con,tail=prev,curr

#         while(right):
#             next_n=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next_n
#             right-=1

#         if con:
#             con.next=prev
#         else:
#             head=prev
        
#         tail.next=curr
#         return head

'''
61. Rotate List
'''
        
# def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
#         if not head:
#             return head
            
#         count=1
#         ptr=head
#         while(ptr.next):
#             ptr=ptr.next
#             count+=1

#         k=k%count
#         ptr.next=head
#         new_end=count-k
#         ptr=head

#         while(new_end>1):
#             ptr=ptr.next
#             new_end-=1

#         head=ptr.next
#         ptr.next=None
        
#         return head
#------------------------------------------
# Another way Not optimal:

 # if not head or k==0:
        #     return head
        # count=0
        # ptr=head
        # while(ptr):
        #     ptr=ptr.next
        #     count+=1
        # print(count)
        # # print(count)
        # k=k%count
        # if count==1 or k==0:
        #     return head
        # head=self.reverseList(head,1,count)
        # head=self.reverseList(head,1,k)
        # head=self.reverseList(head,k+1,count)
        # return head
    
    # def reverseList(self,head,left,right):

    #     if not head or left==right :
    #         return head
        
    #     prev=None
    #     curr=head

    #     while(left>1):
    #         prev=curr
    #         curr=curr.next
    #         left,right=left-1,right-1

    #     con,tail=prev,curr
    #     while(right and curr):
    #         nn=curr.next
    #         curr.next=prev
    #         prev=curr
    #         curr=nn
    #         right-=1
        
    #     if con:
    #         con.next=prev
    #     else:
    #         head=prev
        
    #     tail.next=curr
    #     return head

'''
1290. Convert Binary Number in a Linked List to Integer
'''
# def getDecimalValue(self, head: ListNode) -> int:

#         ptr=head
#         n=0
#         while(ptr):
#             ptr=ptr.next
#             n+=1

#         ptr=head
#         dec=0
#         while(ptr):
#             if ptr.val==1:
#                 dec+=2**(n-1)
            
#             n-=1
#             ptr=ptr.next
        
#         return(dec)


#---------------------------------

        # dec=head.val
        # while(head.next):
        #     dec=dec*2+head.next.val
        #     head=head.next
        
        # return dec

'''
19. Remove Nth node from end of list.
'''
# def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


#         if not head:return head
#         count=n

#         dummy=ListNode()
#         dummy.next=head

#         prev=dummy
#         slow,fast=head,head

#         while(count>0):
#             fast=fast.next
#             count-=1
        
#         while fast:
#             prev=slow
#             slow=slow.next
#             fast=fast.next

#         prev.next=prev.next.next

#         return dummy.next

'''
82. Remove Duplicates from sorted list 2
'''
#         dummy=ListNode()
#         dummy.next=head

#         prev=dummy

#         while head and head.next:
#             if head.val!=head.next.val:
#                 prev=head
#                 head=head.next
#             else:
                
#                 while(head and head.next and head.val==head.next.val):
#                     head=head.next
#                 head=head.next
#                 prev.next=head

#         return(dummy.next)

'''
2. Add 2 numbers
'''

# def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#         dummy=ListNode()
#         curr=dummy
#         carry=0

#         while l1 or l2 or carry:
#             val1=l1.val if l1 else 0
#             val2=l2.val if l2 else 0

#             val=val1+val2+carry
#             carry=val//10
#             val=val%10

#             newNode=ListNode(val)

#             curr.next=newNode
#             curr=curr.next

#             l1=l1.next if l1 else 0
#             l2=l2.next if l2 else 0
        
#         return dummy.next

'''
86. Partition List
'''

#  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

#         h1=small=ListNode()
#         h2=large=ListNode()

#         while(head):

#             if head.val<x:
                
#                 small.next=head
#                 small=small.next

#             else:
                
#                 large.next=head
#                 large=large.next
            
#             head=head.next
        
#         large.next=None
#         small.next=h2.next

'''
21. Merge 2 sorted lists
'''

# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         head=ListNode()
#         curr=head

#         while(list1 and list2):

#             if list1.val<list2.val:
#                 curr.next=list1
#                 curr=curr.next
#                 list1=list1.next
            
#             else:
#                 curr.next=list2
#                 curr=curr.next
#                 list2=list2.next
            
#         curr.next=list1 or list2

#         return head.next

'''
25. Reverse Nodes in k groups
'''
# def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         if not head or not head.next: return head

#         prev=None
#         curr=head

#         count_ptr=head
#         node_count=0

#         while(count_ptr):
#             while(node_count<k and count_ptr):
#                 node_count+=1
#                 count_ptr=count_ptr.next
            
#             if node_count==k:
#                 con,tail=prev,curr
#                 while(node_count>0):
#                     nn=curr.next
#                     curr.next=prev
#                     prev=curr
#                     curr=nn
#                     node_count-=1
                
#                 if con:
#                     con.next=prev
#                 else:
#                     head=prev

#                 tail.next=curr
#                 prev=tail

#         return head

'''
383. Ransom Note
'''
# def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
#         ransom=collections.Counter(ransomNote)
#         mag=collections.Counter(magazine)

#         for i in ransom:
            
#             if ransom[i]>mag[i]:
#                 return False
#         return True


'''
128.  Longest Consecutive Sequence
'''
# def longestConsecutive(self, nums: List[int]) -> int:

#         numset=set(nums)
#         max_seq=0

#         for num in numset:
#             if num-1 not in numset:
#                 seq=1
#                 curr=num
#                 while curr+1 in numset:
#                     seq+=1
#                     curr+=1
                
#                 max_seq=max(max_seq,seq)
#         return max_seq

'''
219. Contains Duplicate 2
'''

#  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

#         index={}
#         for i in range(len(nums)):
#             if nums[i] in index:
#                 if abs(i-index[nums[i]])<=k:
#                     return True
                
#             index[nums[i]]=i
        
#         return False

'''
205. Isomorphic Strings
'''

# def isIsomorphic(self, s: str, t: str) -> bool:
#         # s_ind=[]
#         # t_ind=[]

#         # for i in s:
#         #     s_ind.append(s.index(i))
        
#         # for i in t:
#         #     t_ind.append(t.index(i))
        

#         # if s_ind==t_ind:
#         #     return True
#         # return False

#         s_map={}
#         t_map={}

#         for i in range(len(s)):
#             if s[i] not in s_map and t[i] not in t_map:
#                 s_map[s[i]]=t[i]
#                 t_map[t[i]]=s[i]
            
#             elif s_map.get(s[i])!=t[i] or t_map.get(t[i])!=s[i]:
#                 return False
        
#         return True

'''
202. Happy Number
'''

# def isHappy(self, n: int) -> bool:

#         num=n
#         numsum=set()
        
#         while(num!=1 and num not in numsum):
#             numsum.add(num)
#             digi_sq_sum=0
#             while(num!=0):
#                 rem=num%10
#                 digi_sq_sum+=rem*rem
#                 num=num//10
#             num=digi_sq_sum
        
#         if num==1:
#             return True
#         return False

#######################################################################

'''
Stacks:
'''

'''
20. Valid Parenthesis
'''

# def isValid(self, s: str) -> bool:

#         stack=[]
#         pairs={'(':')','{':'}','[':']'}

#         for i in s:
#             if i in pairs:
#                 stack.append(pairs[i])
#             else:
#                 if not stack:
#                     return False
#                 elif i==stack[-1]:
#                     stack.pop()
#                 else:
#                     return False
        
#         return not stack 

'''
71. Simplify Path
'''

# def simplifyPath(self, path: str) -> str:

#         stack=[]
#         for i in (path.split('/')):
#             if i=='..':
#                 if stack:
#                     stack.pop()
#             elif i=='.' or i=='':
#                 continue
#             else:
#                 stack.append(i)

#         return '/'+'/'.join(stack) 

'''
155. Min Stack
'''

class MinStack:

    def __init__(self):
        self.stack=[]
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val,val])
            return
        curr_min=self.stack[-1][1]
        self.stack.append([val,min(val,curr_min)])
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    
'''
150. Evaluate Reverse Polish Notation
'''

#  def evalRPN(self, tokens: List[str]) -> int:

#         stack=[]
#         op=['+','/','-','*']
#         for tok in tokens:
#             if tok in op:
                
#                 op1=stack.pop()
#                 op2=stack.pop()
                
#                 if tok=='+':
#                     stack.append(op1+op2)
#                 elif tok=='*':
#                     stack.append(op1*op2)
#                 elif tok=='-':
#                     stack.append(op2-op1)
#                 elif tok=='/':
#                     stack.append(int(op2/op1))
#             else:
#                 stack.append(int(tok))
            
#         return(stack[-1])


#############################################################################

'''
100. Same Tree
'''

# def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
        
#         return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


'''
236. Lowest common ancestor
'''
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         # Base Case
#         if not root:
#             return None

#         # First Case => if one of them is root, LCA cannot be after this.
#         if p==root or q==root:
#             return root

#         left=self.lowestCommonAncestor(root.left,p,q)
#         right=self.lowestCommonAncestor(root.right,p,q)

#         # If both left right return something, then one of p and q is in left and other in right
#         if left and right:
#             return root 
        
#         # if only one of them return something, both p and q are present in the same subtree.
#         if left:
#             return left
        
#         return right

'''
101. SYmmetric tree
'''
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

#         if not root:
#             return True

#         def dfs(p,q):
#             if not p and not q:
#                 return True
#             if not p or not q:
#                 return False
#             return p.val==q.val and dfs(p.left,q.right) and dfs(p.right,q.left)
        
#         return dfs(root.left, root.right)


'''
103. Binary Tree Zigzag Level Order Traversal
'''

# def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         level=1
#         queue=deque([root])
#         ans=[]

#         while queue:
#             levelnodes=[]
#             for _ in range(len(queue)):
#                 node=queue.popleft()
#                 levelnodes.append(node.val)

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             # print(levelnodes)
#             if level%2==0:
#                 ans.append(levelnodes[::-1])
#             else:
#                 ans.append(levelnodes)
#             level+=1
        
#         return ans

'''
637. Average of Levels in Binary Tree
'''

# def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
#         queue=deque([root])
#         averages=[]
#         while queue:
#             level_sum=0
#             count=len(queue)
#             for _ in range(len(queue)):
#                 node=queue.popleft()
#                 level_sum+=node.val

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

            
#             averages.append(level_sum/count)

#         return averages