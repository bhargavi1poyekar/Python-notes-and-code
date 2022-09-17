'''
Roman to int
'''

'''
Just add the integer value of each roman
if integer value of curr letter is < int of next , then subtract from the sum, else add 
and add the last digit
'''
# def romanToInt(s):
       
#     roman_int={
#         'I':1,
#         'V':5,
#         'X':10,
#         'L':50,
#         'C':100,
#         'D':500,
#         'M':1000
#     }
    
#     string=list(s)
#     sum=0
#     for i in range(len(string)-1):
#         if roman_int[string[i]]<roman_int[string[i+1]]:  
#             sum-=roman_int[string[i]]
#         else: 
#             sum+=roman_int[string[i]]
    
#     sum+=roman_int[string[-1]]
    
#     return sum

# print(romanToInt('MCMXCIV'))
# print(romanToInt('LVIII'))
# print(romanToInt('III'))

'''
int to roman
'''

'''
rem=num
store the integer values in desc order.
iterate through int values
if rem==0, break
if num is > numeral then rem-=num
roman[]=rom_of_int
'''

# from ast import Num

# num=2018
# int_roman= {1:'I',
#             4:'IV',
#             5:'V',
#             9:'IX',
#             10:'X',
#             40:'XL',
#             50:'L',
#             90:'XC',
#             100:'C',
#             400:'CD',
#             500:'D',
#             900:'CM',
#             1000:'M'}

# rem=num
# roman=[]
# numerals=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
# i=0
# while i<len(numerals):
#     if rem==0:break
#     elif rem>=numerals[i]:
#        rem=rem-numerals[i]
#        roman.append(int_roman[numerals[i]])
#        i=i-1
#     i+=1

# print(''.join(roman))

'''
power of 3
'''
# Multiply with 3 till greater than or equal to number

# def power_of_3(num):

#     prod=1

#     while prod<=num:
#         if prod==num:
#             return True
#         prod*=3
#     return False

# num=81
# print(power_of_3(num))

'''
2 sum
'''

# def twoSum(nums, target):
#     hash_dict={}
    
#     for i in range(len(nums)):
#         if target-nums[i] in hash_dict:
#             return [hash_dict[target-nums[i]],i]
#         else:
#             hash_dict[nums[i]]=i
#     return 'No index adds to target'
            
# print(twoSum([2,7,11,15],14))

'''
Ransom Note
'''

# from collections import Counter
# def ransom_note(ransom,magazine):
    
#     ransom_dict=Counter(ransom)
#     magazine_dict=Counter(magazine)
    
#     for key in ransom_dict:
        
#         if ransom_dict[key]-magazine_dict.get(key,0)>0:
#             return False
#     return True


# print(ransom_note('aabaa','baaa'))

'''
Remove duplicates from sorted array
'''
# nums=[0,0,1,1,1,2,2,3,3,4]

# firs=sec=1

# while sec<len(nums):
#     if nums[sec]==nums[sec-1]:
#         sec+=1
#     else:
#         nums[firs]=nums[sec]
#         firs+=1
#         sec+=1
        
# print(nums[:firs])

'''
Palindrome
'''
# x=12321
# print(str(x)==str(x)[::-1])

'''
Valid Parenthesis
'''
# def valid_par(s):

#     stack=[]

#     for i in range(len(s)):
#         if s[i]=='(':
#             stack.append(')')
#         elif s[i]=='{':
#             stack.append('}')
#         elif s[i]=='[':
#             stack.append(']')
#         else:
#             if len(stack)==0:
#                 return False    # If closing bracket and stack is empty then false 
#             if s[i]!=stack.pop():
#                 return False    #If top of stack is not closing bracket 
    
#     if len(stack)==0:
#         return True
#     else:
#         return False

# print(valid_par('(){}'))
        

'''
Remove element
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
String in String
'''

# def strStr(haystack,needle):
#     idx=0
#     while idx<=len(haystack)-len(needle):
#         if(haystack[idx:idx+len(needle)]==needle):
#             return idx
#         else:
#             idx+=1

# haystack='butsad'
# needle='sad'

# print(strStr(haystack,needle))


'''
Length of Last word

'''

# def len_last_word(s):
#     count=0
#     for i in range(len(s),-1,-1):
#         if s[i]!=' ':
#             count+=1
#         else:
#             if count>=0:  #if space found and count is >0, i.e. not ending in space
#                 break
#     return count

'''
Climbing Stairs
'''

# def climb_stair(n):
    
#     if n<=2:
#         return n
    
#     fir=1
#     sec=2
#     ways=0
#     for i in range(3,n+1):
#         ways=fir+sec
#         fir=sec
#         sec=ways
    
#     return ways

# print(climb_stair(5))    

'''
Rotate 3*3 matrix
'''

# import numpy as np
# matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix)
# n=len(matrix)

# j=0
# for i in range(0,n-1):
#     top=matrix[j][i]
#     matrix[j][i]=matrix[n-i-1][j]
#     matrix[n-i-1][j]=matrix[n-1][n-i-1]
#     matrix[n-1][n-i-1]=matrix[i][n-1]
#     matrix[i][n-1]=top
    
# print(matrix)

'''
Find missing element
'''

# def missingNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
    
#     n=len(nums)
#     expected_sum=n*(n+1)/2
#     sum_now=sum(nums)
#     return expected_sum-sum_now

# print(missingNumber([3,0,1]))

'''
Move Zeroes
'''

# def moveZeros(nums):
    
#     idx=0
#     for i in range(len(nums)):
#         if nums[i]!=0:
#             nums[idx]=nums[i]
#             idx+=1
        
#     return nums[0:idx]

# print(moveZeros([1,0,2,0,0,3,0]))


'''
Max subarray
'''

# def max_subarray(nums):
    
#     total=0
#     max_sum=-100
#     for i in range(len(nums)):
#         total+=nums[i]
        
#         if max_sum<total:
#             max_sum=total
        
#         if total<0:
#             total=0
            
#     return max_sum

'''
Container with most water
'''

# Brute Force O(n^2)

# def maxArea(height):
    
#     maxarea=0
#     for i in range(len(height)):
#         for j in range(1,len(height)):
#             ht=min(height[i],height[j])
#             wid=abs(i-j)
#             area=ht*wid
#             if maxarea<area:
#                 maxarea=area
#     return maxarea

# print(maxArea([1,1])) 

# Optimized solution O(n)

# def maxArea(height):
#     maxarea=0
#     n=len(height)
#     start=0
#     end=n-1

#     while start!=end:
        
#         area=min(height[start],height[end])*abs(end-start)
#         maxarea=max(area,maxarea)
#         if height[start]<height[end]:
#             start+=1
#         else:
#             end-=1

#     return(maxarea)

# print(maxArea([1,8,6,2,5,4,8,3,7]))
'''
Search Insert position
'''

## Binary Search 

# def searchInsert(, nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
    
#     if target<nums[0]:
#         return 0
#     elif target>nums[-1]:
#         return len(nums)
    
#     left=0
#     right=len(nums)-1
#     mid=(len(nums)-1)//2
    
#     while left-right!=0:
        
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]>target:
#             right=mid
#         else:
#             left=mid+1
            
#         mid=abs(right+left)//2
#     return mid
# print(searchInsert([1,3,5,6],7))
            
'''
Majority Element
'''
# def majorityElement(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     count={}
    
#     for i in nums:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
    
#     limit=len(nums)/2
    
#     for i in count:
#         if count[i]>limit:
#             return i

# print(majorityElement([1,1,1,2,2]))

'''
Merge Sorted Array
'''
# def merge( nums1, m, nums2, n):
#     """
#     :type nums1: List[int]
#     :type m: int
#     :type nums2: List[int]
#     :type n: int
#     :rtype: None Do not return anything, modify nums1 in-place instead.
#     """

        # Use Insertion Sort  
#     for i in range(n):
        
#         key=nums2[i]
        
#         j= m+i-1
        
#         while j>=0 and key<nums1[j]:
            
#             nums1[j+1]=nums1[j]
#             j-=1
        
#         nums1[j+1]=key
#     return nums1     

# print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))       
        
'''
Intersection of 2 Arrays
'''

# def intersection(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     inter=[]
#     for i in range(len(nums1)):
#         if nums1[i] in nums2 and nums1[i] not in inter:
#             inter.append(nums1[i])
    
#     return inter

'''
Minimum Sum of Four Digit Number After Splitting Digits
'''

# def minimumSum(num):
#     """
#     :type num: int
#     :rtype: int
#     """
#     digits=[int(i) for i in str(num)]
#     digits.sort()
#     num1=digits[0]*10+digits[3]
    
#     num2=digits[1]*10+digits[2]
    
#     return num1+num2
# print(minimumSum(1234))


'''
How many numbers are smaller than the correct number?
'''
# def smallerNumbersThanCurrent(nums):
    
#     sort_nums=sorted(nums) # sort and store in diff arr
#     count_dict={} # hash to store the count of nums smaller
#     n=len(nums) 
#     count_dict[sort_nums[0]]=0 # first count
#     for i in range(1,n):
#         if sort_nums[i]!=sort_nums[i-1]: # if both are same, count is not written
#             count_dict[sort_nums[i]]=i # for unique elements, count is index 

#     fin_count=[0]*n 
#     for i in range(n): # sort the count acc to nums
#         fin_count[i]=count_dict[nums[i]]
#     return fin_count

# print(smallerNumbersThanCurrent([8,1,2,2,3]))

'''
Sorting the Sentence
'''


# from collections import OrderedDict
# def sortSentence(s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         sent_list=s.split()
    
#         position={}
#         for i in range(len(sent_list)):
#                 position[sent_list[i][-1]]=i
        
#         sorted_pos=OrderedDict(sorted(position.items()))
        
#         sort_sent=[]
#         for i in sorted_pos:
#                 sort_sent.append(sent_list[sorted_pos[i]][:-1])
        
#         return ' '.join(sort_sent)


# print(sortSentence('is2 sentence4 This1 a3'))

'''
Build Array from Permutation
'''
# def buildArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # ans=[0]*len(nums)

#         # for i in range(len(nums)):
#         #     ans[i]=nums[nums[i]]

#         #         ans=[nums[nums[i]] for i in range(len(nums))]

#         return [nums[i] for i in nums]



'''
75-Day
'''
# # Day 1- Array- Running Sum

# def runningSum(nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         sum=[0]*len(nums)
#         sum[0]=nums[0]
#         for i in range(1,len(nums)):
#                 sum[i]=sum[i-1]+nums[i]

# # Day 1- Find Pivot Index

# def pivotIndex(self, nums):
#         # nums=[-1,-1,0,1,1,-1]
#         n=len(nums)
#         leftsum=[0]*(n+1)
        
#         leftsum[0]=0
#         for i in range(1,n+1):
#             leftsum[i]=leftsum[i-1]+nums[i-1]
        
#         for i in range(n):
#             if leftsum[i]==leftsum[n]-leftsum[i+1]:
#                 return i
#         if leftsum[n-1]==0:
#             return n-1
#         return -1

# Day -2 Strings

# Isomorphic Strings

# def isIsomorphic(s,t):
#         s_idx=[]
#         t_idx=[]
        
#         for i in s:               
#                 s_idx.append(s.index(i)) #adds index of first occurence of letter
#         for i in t:
#                 t_idx.append(t.index(i))
#         if s_idx==t_idx:
#                 return True
#         return False
              
# print(isIsomorphic('paper','title')) 

# # is Subsequence

# def isSubsequence(s, t):

#         s_ptr=0
#         t_ptr=0
        
#         while s_ptr<len(s) and t_ptr<len(t):
            
#             if s[s_ptr]==t[t_ptr]:
#                 s_ptr+=1
#             t_ptr+=1
        
#         if s_ptr==len(s):
#             return True
#         return False

# Day 3- Linked List

# Merge 2 LL:
# def mergeTwoLists(list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         cur = dummy = ListNode()
#         while list1 and list2:               
#         if list1.val <= list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#         else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#         cur.next = list1 if list1 else list2
        
#         return dummy.next


#  Reverse Linked List

# def reverseList(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
    
#     prev=next=None
#     curr=head
    
#     while curr:
        
#         next=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next
    
#     head=prev
#     return head