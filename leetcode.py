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
Number Of good Pairs
'''
# def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count=0
#         count_hash=Counter(nums)
#         for i in count_hash:
#             count+=count_hash[i]*(count_hash[i]-1)//2
        
#         return count

'''
Kids with greatest Number Of Candies:
'''

# def kidsWithCandies(self, candies, extraCandies):
        
#         max_candies=max(candies)
        
#         ans=[]
#         for i in candies:
#             if i+extraCandies>=max_candies:
#                 ans.append(True)
#             else:
#                 ans.append(False)
            
#         return ans

'''
Decompress Run-Length Encoded List
'''
# def decompressRLElist(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans=[]
#         i=0
#         # if len(nums)<=2:
#         #     ans.extend([nums[(2*i)+1]]*nums[2*i])
#         for i in range(0,len(nums)-1,2):
#             ans.extend([nums[i+1]]*nums[i])
        
#         return(ans)


'''
Sum of Even Numbers After Queries
'''
# Find even sum of nums in the start, and then only change the even sum when nums is changing 

# def sumEvenAfterQueries(nums, queries):
#         """
#         :type nums: List[int]
#         :type queries: List[List[int]]
#         :rtype: List[int]
#         """
#         even_sum=0
#         answers=[]
#         for i in nums:
#             if i%2==0:
#                 even_sum+=i
                
#         for i in queries:
#             if nums[i[1]]%2==0:
#                 even_sum-=nums[i[1]]
#             nums[i[1]]=nums[i[1]]+i[0]
#             if nums[i[1]]%2==0:
#                 even_sum+= nums[i[1]]
#             answers.append(even_sum)
        
#         return answers
            
        # Brute Force- Very bad idea
        
#         answers=[]
        
#         for i in queries:
#             nums[i[1]]=nums[i[1]]+i[0]
#             sum=0
#             for j in nums:
#                 if j%2==0:
#                     sum+=j
#             answers.append(sum)
        
#         return(answers)

# '''
# Longest Palindrome
# '''
# from collections import Counter
# s= 'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'

# def longestPalindrome(s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # s=s.upper()
#         s_count=Counter(s)
#         print(s_count)
#         flag=True
#         pal_len=0
#         for i in s_count:
#             if s_count[i]%2==0:
#                 pal_len+=s_count[i]
#             else:
#                 if flag: 
#                         flag=False
#                         pal_len+=(s_count[i])
#                 else:
#                         pal_len+=(s_count[i]-1)
        
#         return pal_len

# print(longestPalindrome(s))

'''
Reverse Strings-3
'''
# def reverseWords(s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s_list=s.split(' ')
#         s_reverse=' '.join([i[::-1] for i in s_list])
#         return s_reverse

# print(reverseWords("Let's take LeetCode contest"))

'''
Concatenation of consecutive Binary Numbers
'''

# def concatenatedBinary(n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         bin_list=[]
#         for i in range(1,n+1):
                
#                 bin_list.append(bin(i)[2:])
        
#         bin_con=''.join(bin_list)
#         mod=10**9 +7
#         print(int(bin_con,2)%mod)
        
# print(concatenatedBinary(3))

'''
First Hard Quest- Median of Two Sorted Arrays
'''

# def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
        
#         # nums1=[1,2]
#         # nums2=[3,4]
        
#         tot_len=len(nums1)+len(nums2)
#         even=0
#         if tot_len%2==0:
#             even=1
        
#         if even:
#             mid1=(tot_len//2)-1
#             mid=(tot_len//2)
#         else:
#             mid=(tot_len//2)
            
        
#         count=0
#         i=0
#         j=0
#         merge=[]
        
#         while i!=len(nums1) and j!=len(nums2) and count!=mid+1:
#             if nums1[i]<=nums2[j]:
#                 merge.append(nums1[i])
#                 i+=1
                
#             else:
#                 merge.append(nums2[j])
#                 j+=1
#             count+=1
        
        
        
#         if count!=mid+1:
#             if i!=len(nums1):
#                 merge.extend(nums1[i:])
#             elif j!=len(nums2):
#                 merge.extend(nums2[j:])
       
#         if even:
           
#             return (float(merge[mid1]+merge[mid])/2)
#         else:
#             return (merge[mid])

'''
Find Winner on a Tic Tac Toe Game
'''

# def tictactoe(self, moves):
#         """
#         :type moves: List[List[int]]
#         :rtype: str
#         """
#         # moves=[[0,0],[2,2],[1,0],[2,0],[0,1],[1,2],[1,1],[0,2]]
#         Win=[[[0,0],[1,1],[2,2]],
#             [[0,0],[0,1],[0,2]],
#              [[0,0],[1,0],[2,0]],
#              [[0,1],[1,1],[2,1]],
#              [[0,2],[1,1],[2,0]],
#              [[0,2],[1,2],[2,2]],
#              [[1,0],[1,1],[1,2]],
#              [[2,0],[2,1],[2,2]]
#             ]
#         A_moves=[]
#         B_moves=[]
        
#         for i in range(len(moves)):
#             if i%2==0:
#                 A_moves.append(moves[i])
#             else:
#                 B_moves.append(moves[i])
        
#         for i in Win:
#             print(B_moves)
#             print(i)
#             if all(x in A_moves for x in i):
#                 return 'A'
#             elif all(x in B_moves for x in i):
#                 return 'B'
        
#         if len(moves)==9:
#             return 'Draw'
#         return 'Pending'

'''
Find First and Last Position of Element in Sorted Array
'''
# Perform binary search 3 times, first for finding one of the index of target, 
# then finding left position and then finding right

# def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        
#         start, end=0, len(nums)-1
#         found=-1
        
#         while start<=end:
            
#             mid=(start+end)//2
            
#             if nums[mid]==target:
#                 found=mid
#                 break
#             elif nums[mid]>target:
#                 end=mid-1
#             else:
#                 start=mid+1
        
#         if found==-1:
#             return [-1,-1]
        
#         # find left boundary
#         start, end=0, found
#         while start<=end:
#             mid=(start+end)//2
#             if nums[mid]==target:
#                 end=mid-1
#             else:
#                 start=mid+1
        
#         left=start
        
#         # find right boundary
        
#         # find left boundary
#         start, end=found, len(nums)-1
#         while start<=end:
#             mid=(start+end)//2
#             if nums[mid]==target:
#                 start=mid+1
#             else:
#                 end=mid-1
        
#         right=end
        
#         return [left,right]
        
'''
Add 2 Numbers of linked list
'''
# def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         # Getiing num1
#         count=0
#         num1=0
#         while l1!=None:
#             num1+=(10**count)*l1.val
#             l1=l1.next
#             count+=1
        
#         # Getting num2
#         count=0
#         num2=0
#         while l2!=None:
#             num2+=(10**count)*l2.val
#             l2=l2.next
#             count+=1
        
#         ans=num1+num2
        
#         sum_nums=ListNode()
#         start=sum_nums
#         rem=ans%10
#         sum_nums.val=rem
#         ans=ans//10
        
#         while ans!=0:
#             sum_nums.next=ListNode(None)
#             sum_nums=sum_nums.next
#             rem=ans%10
#             ans=ans//10
#             sum_nums.val=rem
        
#         return start

'''
Count number of pairs with abs diff k
'''

# def countKDifference(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
        
#         diff_count={}
#         count=0
        
#         for i in nums:
            
#             if i in diff_count:
#                 count+=diff_count[i]
#             if i>k:
#                 if abs(k-i) in diff_count:
#                     diff_count[abs(k-i)]+=1
#                 else:
#                     diff_count[abs(k-i)]=1
                    
#             if (k+i) in diff_count:
#                 diff_count[k+i]+=1
#             else:
#                 diff_count[k+i]=1
            
        
#         return(count)


'''
Fibonacci Numbers
'''

# def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        # O(2^n)
        # Recursive solution
        # if n<=1:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        # -------------
        
        # O(n)
        # Iterative Solution- Dynamic Programming solution
        # if n==0:
        #     return n
        # if n==1 or n==2:
        #     return 1
        
        # fib0,fib1,fib2=0,1,1
        
        # for i in range(2,n+1):
        #     fib2=fib0+fib1
        #     fib0=fib1
        #     fib1=fib2
        
        # return fib2
        

'''
Balanced Strings
'''

# def balancedStringSplit(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         r_count=0
#         l_count=0
        
#         split_count=0
        
#         for i in s:
#             if i=='R':
#                 r_count+=1
#             elif i=='L':
#                 l_count+=1
            
#             if r_count==l_count:
#                 split_count+=1
#                 r_count=0
#                 l_count=0
        
#         return split_count

'''
Minimum Amount of Time to Collect Garbage
'''
# def garbageCollection(self, garbage, travel):
#         """
#         :type garbage: List[str]
#         :type travel: List[int]
#         :rtype: int
#         """
        
#         g_end_idx, p_end_idx, m_end_idx=0,0,0
        
#         for i in range(len(garbage)-1, -1,-1):
#             if 'G' in garbage[i]:
#                 g_end_idx=i
#                 break
            
#         for i in range(len(garbage)-1, -1,-1):
#             if 'P' in garbage[i]:
#                 p_end_idx=i
#                 break
        
#         for i in range(len(garbage)-1, -1,-1):
#             if 'M' in garbage[i]:
#                 m_end_idx=i
#                 break
#         g_time=0
        
#         for i in range(g_end_idx+1):
#             g_time+=garbage[i].count('G')
#             if i+1<=g_end_idx:
#                 g_time+=travel[i]
#         p_time=0
#         for i in range(p_end_idx+1):
#             p_time+=garbage[i].count('P')
#             if i+1<=p_end_idx:
#                 p_time+=travel[i]
                
#         m_time=0
#         for i in range(m_end_idx+1):
#             m_time+=garbage[i].count('M')
#             if i+1<=m_end_idx:
#                 m_time+=travel[i]
            
#         return g_time+p_time+m_time

