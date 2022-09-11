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