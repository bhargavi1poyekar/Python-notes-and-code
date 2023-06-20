'''
1. Merge Sorted Arrays:
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
2. Remove element
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
3. Remove Duplicates form Sorted Array
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
4. Remove Duplicates from Sorted Array 2
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
5. Majority Element
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
6. Rotate Array
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
7. Best Time to Buy and Sell Stock
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
8. Best Time to Buy and Sell Stock 2
'''

# the most important thing here is to know that the all valleys and peaks need to be considered, hence immediate up and down prices are considered.

#  def maxProfit(self, prices: List[int]) -> int:

#         profit_max=0

#         for i in range(0,len(prices)-1):
#             if prices[i+1]>prices[i]:
#                 profit_max+=prices[i+1]-prices[i]
        
#         return profit_max

'''
9. Jump Game
'''

# def canJump(self, nums: List[int]) -> bool:
        
#         n=len(nums)-1

#         for i in range(n-1,-1,-1):
#             if i+nums[i]>=n:
#                 n=i
           
#         return True if n==0 else False

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

