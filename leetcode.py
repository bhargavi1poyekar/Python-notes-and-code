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

'''Hackerranke Ransomnote'''
# m_words=Counter(magazine)
# n_words=Counter(note)

# for i in n_words:
# if i not in m_words or n_words[i]>m_words[i]:
#         return "No"
# return "Yes"



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

'''
Number of 1 bits
'''
# def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         n_bin=bin(n)[2:]
#         return(n_bin.count('1')

'''
Longest nice substring- nice if the substring has both uppercase and lowercase of the letters present
'''
# def longestNiceSubstring(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
    
#         nice=''
#         for i in range(len(s)+1):
#             for j in range(len(s)+1):
#                 substr=s[i:j]
                
#                 if self.isNice(substr):
#                     print(substr)
#                     nice=max(nice,substr, key=len)
                
#         return nice
    
#     def isNice(self,s):
        
#         char_count=Counter(s)
        
#         for i in char_count:
#             if i.upper() not in s or i.lower() not in s:
#                 return False
#         return True

# Divide and Conquer approach:

# def longestNiceSubstring(s):
#         """
#         :type s: str
#         :rtype: str
#         """
    
#         idx=isNice(s)
#         if idx==-1:
#                 return s
        
#         opt1=longestNiceSubstring(s[0,idx])
#         opt2=longestNiceSubstring(s[idx+1,len(s)])
        
#         return max(opt1,opt2,key=len)
    
# def isNice(s):

#         char_pos={}
        
#         for i in range(len(s)):
#                 char_pos[s[i]]=i

#         for i in char_pos:
#                 if i.upper() not in s or i.lower() not in s:
#                         return char_pos[i]
#         return -1


# print(longestNiceSubstring('Bb'))

'''
Min moves to seat everyone
'''

# def minMovesToSeat(self, seats, students):
#         """
#         :type seats: List[int]
#         :type students: List[int]
#         :rtype: int
#         """
#         seats=sorted(seats)
#         students=sorted(students)
        
#         moves=0
#         for i in range(len(students)):
#             moves+=abs(students[i]-seats[i])
        
#         return moves

'''
Largest Local values in a Matrix
'''

# def largestLocal(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: List[List[int]]
#         """
        
#         max_arr=[]
        
#         for i in range(1,len(grid)-1):
#             temp=[]
#             for j in range(1,len(grid)-1):
#                 max_loc=max(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1])
#                 temp.append(max_loc)
#             max_arr.append(temp)

'''
Arrange the listin decreasing order of they=ir frequencies
'''
# import collections
# listEle=[1,2,2,3,3,3,4,4,5,5,5,5,6,6,6,7,8,9,10]

# count_list=collections.Counter(listEle)
# res=[]
# for i in count_list:
        
#         for j in range(count_list[i]):
#                 res.append(i)
# print(res)

'''
Push Dominoes:
'''

# States for the dominoes:
        #   • Any triplet that reaches the state 'R.L' remains
        #     that state permanently.
        #  
        #   • These changes occur to pairs that are not part of an 'R.L':
        #     'R.' --> 'RR', .L' --> 'LL'

        #  Here's the plan:
        #    1) To avoid the problem with the 'R.L' state when we  address the 
                                #       'R.' --> 'RR' and  '.L' --> 'LL' changes, we replace each 'R.L' 
                                #.       with a dummy string (say, 'xxx').
        #       
        #    2) We perform the 'R.' --> 'RR', .L' --> 'LL' replacements.

        #    3) Once the actions described in 1) and 2) are completed, we repeat 
        #       until no changes occur. We replace the dummy string with 'R.L'. 
# def pushDominoes(self, dominoes: str) -> str:
#         temp = ''

#         while dominoes != temp:
#                 temp = dominoes
#                 dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
#                 dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
#                 dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

#         return  dominoes.replace('xxx', 'R.L')              # <-- 3)

'''
Remove Nth node from end of list
'''
# def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
        
#         temp=temp2=temp3=head
        
#         count=1
#         while temp.next!=None:
#             temp=temp.next
#             if count>=n:
#                 temp2=temp2.next
#             count+=1
        
#         if temp2==head:
#             temp3=temp2.next
#             return temp3
        
#         else:
#             while temp3.next!=temp2:
#                 temp3=temp3.next
#             temp3.next=temp2.next
        
#         return head

'''
Backspace String Compare
'''
# def backspaceCompare(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         # s='y#fo##f'
#         # t='y#f#o##f'
        
#         s_stack=[]
#         t_stack=[]
        
#         for i in s:
#             if i=='#' and len(s_stack)>0:
#                 s_stack.pop()
#             elif i!='#':
#                 s_stack.append(i)
        
#         print(s_stack)
#         for i in t:
#             if i=='#' and len(t_stack)>0:
#                 t_stack.pop()
#             elif i!='#':
#                 t_stack.append(i)
#         print(t_stack)
#         if s_stack==t_stack:
#             return True
#         return False

'''
Find K closest elements
'''
# def findClosestElements(self, arr, k, x):
#         """
#         :type arr: List[int]
#         :type k: int
#         :type x: int
#         :rtype: List[int]
#         """
        
#         diff=[(abs(x-n),i) for i,n in enumerate(arr)]
#         diff=sorted(diff)
#         print(diff)
#         result=[arr[i[1]] for i in diff[:k]]
#         return sorted(result)

'''Linked List Remove Duplicates'''

# def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if head is None:
#             return
        
#         tempNode=head
        
#         vis=set([tempNode.val])
        
#         while tempNode.next:
#             if tempNode.next.val in vis:
#                 tempNode.next=tempNode.next.next
#             else:
#                 vis.add(tempNode.next.val)
#                 tempNode=tempNode.next
        
#         return head

'''
Find Largest Perimeter of Triangle
'''
# def largestPerimeter(self, nums: List[int]) -> int:
        
#         sorted_nums=sorted(nums,reverse=True)
        
#         for i in range(len(sorted_nums)-2):
#             if sorted_nums[i]<sorted_nums[i+1]+sorted_nums[i+2]:
#                 return sorted_nums[i]+sorted_nums[i+1]+sorted_nums[i+2]
        
#         return 0

'''
 Group the People Given the Group Size They Belong To
'''

# def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
#         buckets={}
        
#         for i in range(len(groupSizes)):
            
#             if groupSizes[i] not in buckets:
#                 buckets[groupSizes[i]]=[[i]]
#             else:
                
#                 if len(buckets[groupSizes[i]][-1])<groupSizes[i]:
#                     buckets[groupSizes[i]][-1].append(i)
#                 else:
#                     buckets[groupSizes[i]].append([i])
            
#         ans=[]

'''
Count and Say 
'''

# def countAndSay(self, n: int) -> str:
#         if n==1:
#             return '1'
#         else:
#             say=self.countAndSay(n-1)
#             count_say=[]
#             count=1
#             if len(say)==1:
#                 count_say.append([1,say[0]])
#             else:
                
#                 for i in range(0,len(say)-1):
#                     if say[i]==say[i+1]:
#                         if i==len(say)-2:
#                             count+=1
#                             count_say.append([count,say[i]])
#                         else:
#                             count+=1
#                     else:
#                         count_say.append([count,say[i]])
#                         count=1
#                 if say[-1]!=say[-2]:
#                     count_say.append([1,say[-1]])
            
#             say_string=''
#             for i in count_say:
#                 say_string+=str(i[0])+str(i[1])
            
#             return say_string

'''
Top K Frequent words
'''
# def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         Count_hash={}
        
#         for i in words:
#             if i not in Count_hash:
#                 Count_hash[i]=1
#             else:
#                 Count_hash[i]+=1
        
#         print(Count_hash)
        
#         count_list=[]
#         for i in Count_hash:
#             count_list.append([i,Count_hash[i]])
        
#         print(count_list)
        
#         count_list_sorted=sorted(count_list, key=lambda l:(-l[1],l[0]))
        
#         return [x[0] for x in count_list_sorted[:k]]
        
'''
Guess Number Higher or Lower
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# class Solution:
#     def guessNumber(self, n: int) -> int:
#         low=1
#         high=n
#         mid=n//2
        
#         while True:
#             ans=guess(mid)
#             if ans==-1:
#                 high=mid
#             elif ans==1:
#                 low=mid+1
#             else:
#                 return mid
#             mid=(low+high)//2

'''
Paypal OA 2
'''
# vowels=['a','e','i','o','u']
# strArr=['aba','bcb','ece','aa','e']
# strArr=['aab','a','bcd','awe','bbbbbu']
# queries=['1-3','2-5','2-2']
# queries=['2-3','4-5']

# count=[0]*len(queries)
# for i in range(len(queries)):
#         query=queries[i]
#         l=int(queries[i][0])-1
#         r=int(queries[i][2])-1
#         print(f'l={l},r={r}')
#         for j in range(l,r+1):
#                 if strArr[j][0] in vowels and strArr[j][-1] in vowels:
#                         count[i]+=1
# print(count)
       
'''
Paypal OA1
'''
# songs=[40,20,60]
# count=0
# for i in range(len(songs)):
#         for j in range(i+1,len(songs)):
                
#                 if (songs[i]+songs[j])%60==0:
#                         count+=1
# print(count)

# count=0
# pair_dict={}
# for i in range(len(time)):
#         # print(time[i])
#         if -time[i]%60 in pair_dict:
#         count+=pair_dict[-time[i]%60]
#         if time[i]%60 in pair_dict:
#         pair_dict[time[i]%60]+=1
#         else:
#         pair_dict[time[i]%60]=1
#         # print(pair_dict)
#         # print(count)
        
# # print(pair_dict)
# return(count)

'''
Tu simple - Rachit
Q1
'''

# import sys
# A=12
# B=21
# N=5

# end=2**N
# max_val=0
# X_val=0

# # while(start<end):
# #         # X=(start+end)//2
        
# #         print(X,)
# #         start+=1
# #         X+=1
# mod=(10**9)+7
# for i in range(end):
#         if max_val<=(A^i)*(B^i):
#                 max_val=(A^i)*(B^i)
#                 X_val=i

# print(max_val%mod)

'''
Minimum number of arrows to burst balloons
'''

# def findMinArrowShots(self, points: List[List[int]]) -> int:
        
#         points.sort(key=lambda x:x[1])
        
#         count=1
#         end_ptr=points[0][1]
#         for s,e in points:
#             if s>end_ptr:
#                 end_ptr=e
#                 count+=1
#         return count

'''Minimum moves to equal array elements
'''

# def minMoves(self, nums: List[int]) -> int:

#         minim=min(nums)

#         moves=0

#         for i in nums:
#                 moves+=i-minim
#         return moves

'''
Generate Parenthesis
'''

# def dfs(left, right, s):
#             if len(s) == n * 2:
#                 res.append(s)
#                 return 

#             if left < n:
#                 dfs(left + 1, right, s + '(')

#             if right < left:
#                 dfs(left, right + 1, s + ')')

#         res = []
#         dfs(0, 0, '')
#         print(res)

'''
Same Tree
'''
# def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
#         if not p and not q:
#             return True
#         if p and q and p.val==q.val:
#             return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
#         else:
#             return False

'''
Symmetric Tree
'''
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #         return True
        # def traverse(l,r):
        #         if not l and not r:
        #         return True
        #         if not l or not r:
        #         return False
        #         if l.val ==r.val:
        #         return traverse(l.left,r.right) and traverse(l.right,r.left)
        #         return False

        # return traverse(root.left, root.right)

'''
Finding the Users Active Minutes
'''

#  def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
#         hash={}

#         for Id, time in logs:
#             if Id in hash:
#                 hash[Id].append(time)
#             else:
#                 hash[Id]=[time]
        
#         ans=[0]*k
#         for Id in hash:
#             ans[len(set(hash[Id]))-1]+=1
#         return ans

'''
Leet-152: Maximum product subarray
'''

# def maxProd(arr):
#     res=max(arr)
#     curMin, curMax=1,1
#     for n in arr:
#         if n==0:
#             curMax,curMin=1,1
#             continue
#         tmp=curMax*n
#         curMax=max(n*curMax,n*curMin,n)
#         curMin=min(tmp,n*curMin,n)
#         res=max(res,curMax)
#      return res

'''
Count Negative Numbers in a Sorted Matrix

'''
# def countNegatives(self, grid: List[List[int]]) -> int:
#         rows,cols=len(grid),len(grid[0])
#         count=0
#         row=rows-1
#         col=0

#         while row>=0 and col<cols:
#             if grid[row][col]<0:
#                 count+=cols-col
#                 row-=1
#             else:
#                 col+=1
        
#         return count

'''
Find Smallest Letter greater than target
'''

# def nextGreatestLetter(self, letters: List[str], target: str) -> str:

#         # for i in letters:
#         #     if ord(i)>ord(target):
#         #         return i
#         # return letters[0]

#         left=0
#         right=len(letters)-1
#         while(left<=right):
#             mid=(right-left//2)
#             if ord(letters[mid])>ord(target):
#                 right=mid-1
#             else:
#                 left=mid+1
        
#         if left==len(letters):
#             return letters[0]
#         return letters[left]

'''
Find the Highest ALtitude
'''

#  def largestAltitude(self, gain: List[int]) -> int:
        
#         n=len(gain)
        
#         curr_alt=0
#         max_alt=0
#         for i in range(n):
#             curr_alt=gain[i]+curr_alt
#             max_alt=max(max_alt,curr_alt)
#         return max_alt

'''
K Radius SubArray Averages
'''

#  def getAverages(self, nums: List[int], k: int) -> List[int]:

#         num_count=(k*2)+1
#         ans=[0 for i in range(len(nums))]

#         prefix_sum=[0]
#         for i in range(len(nums)):
#             prefix_sum.append(prefix_sum[i]+nums[i])

#         # print(prefix_sum)

#         for i in range(len(nums)):
#             if i-k<0 or i+k>len(nums)-1:
#                 ans[i]=-1
#             else:
#                 ans[i]=(prefix_sum[i+k+1]-prefix_sum[i-k])//num_count
        
#         return(ans)

'''
Substrings of size 3 with distinct characters
'''

#  def countGoodSubstrings(self, s: str) -> int:


#         count=0
#         for i in range(len(s)-2):
#             if s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]:
#                 count+=1
            
#         return count

 