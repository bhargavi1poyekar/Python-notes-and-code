
'''
485. Max Consecutive Ones
'''

# count=0
# max_count=-1
# for i in nums:
#         if i==1:
#         count+=1
#         else:
#         max_count=max(max_count,count)
#         count=0
# max_count=max(count,max_count)
# return max_count

'''
If 1 increment count, else store the count if it is max till now. 
'''

'''
1295. Find Numbers with even number of digits
'''
# def findNumbers(self, nums: List[int]) -> int:
        
#         digi_count=[0 for i in range(len(nums))]
#         even_count=0
#         for i in range(len(nums)):
#             while(nums[i]!=0):
#                 nums[i]=nums[i]//10
#                 digi_count[i]+=1
#             if digi_count[i]%2==0:
#                 even_count+=1
#         return even_count
# print(findNumbers([555,901,482,1771]))

'''
For every number find the number of digits, dividing by 10 till it gets to 0.
'''
        

'''
977. Squares of sorted array => O(n)
''' 

# def sortedSquares(self, nums: List[int]) -> List[int]:
        
#         n=len(nums)
#         left=0
#         right=n-1
#         index=n-1
#         result=[0 for i in range(n)]
        
#         while(index>=0):
#             if abs(nums[left])>abs(nums[right]):
#                 result[index]=nums[left]*nums[left]
#                 left+=1
#             else:
#                 result[index]=nums[right]*nums[right]
#                 right-=1
            
#             index-=1
        
#         return result

'''
2 ptr approach-> Since it is sorted, keep 1 ptr at start and one at end.
Compare the absolute values, and store the square of greater number in final result array from the end.  
'''

'''
1089. Duplicate Zeros in place
'''

# def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
        
#         zeroes = arr.count(0)
#         n = len(arr)
#         for i in range(n-1, -1, -1):
#             if i + zeroes < n:
#                 arr[i + zeroes] = arr[i]
#             if arr[i] == 0: 
#                 zeroes -= 1
#                 if i + zeroes < n:
#                     arr[i + zeroes] = 0

'''
1. Start a ptr from back, and keep the count of zeros. 
2. Check if ptr+ zeros is less than n (if not, then that value will not be in the final array.)
If yes then add it to the ptr+zero_count index.
3. If you get a zero, decrement the count of zero, and check again, if the ptr + 0count is less than n.
If yes then add a zero at i+0count index
'''

'''
88. Merge Sorted Arrays:
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

2. Check if there are more numbers left in nums2. Add it to the beginning. 
'''

'''
27. Remove element
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
1346. Check if N and its double exists
'''

# def checkIfExist(self, arr: List[int]) -> bool:
    
#     hash_tab={}
#     for i in arr:
#         if (2*i in hash_tab) or (i%2==0 and i//2 in hash_tab):
#             return True
#         hash_tab[i]=1
#     return False

'''
Keep a hashmap to maintain the values. 
Before adding values, check if double of that number or half of the number (if even) already present in hashtab.
'''

'''
941. Valid Mountain Array
'''

# def validMountainArray(self, arr: List[int]) -> bool:
    
#     if len(arr)<3:
#         return False
#     n=len(arr)
#     change=0
    
#     while(change<n-1 and arr[change]<arr[change+1]):
#         change=change+1
    
#     if change==0 or change==n-1:
#         return False
    
#     while(change<n-1 and arr[change]>arr[change+1]):
#         change=change+1
    
#     if change==n-1:
#         return True
#     else:
#         return False


'''
Keep a count var. Increment it till array is increasing. 
After it stops increasing, check if the count is still at beginning or end. 
If yes, then false because beginning means(not increasing) and end means (not decreasing).
Again increment the var till it decreases. CHeck if it reached the end. yes, then return true
If it doesnt reach end, it means it is again increasing. retur false
'''

'''
1299. Replace Elements with greatest elements on right side
'''

# def replaceElements(self, arr: List[int]) -> List[int]:
        
#         max_elem=arr[len(arr)-1]
#         arr[len(arr)-1]=-1
#         for i in range(len(arr)-2,-1,-1):
#             temp=arr[i]
#             arr[i]=max_elem
#             max_elem=max(max_elem,temp)
        
#         return arr

'''
Start from end. keep a var for greatest element. Keep the current element in temp. 
replace curr with max element and then compare the temp with max to get the new max. 
'''


'''
283. Move Zeros in the end
'''

# def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         ptr1=0
#         ptr2=0
        
#         n=len(nums)
#         count=0
        
#         while ptr2<n:
#             if nums[ptr2]!=0:
#                 nums[ptr1]=nums[ptr2]
#                 ptr1+=1
#                 ptr2+=1
#             else:
#                 count+=1
#                 ptr2+=1
        
#         nums[ptr1:ptr1+count]=[0 for i in range(count)]


'''
2 ptr approach. fast and slow ptr. 
increment fast ptr till you get to a value not equal to 0. 
Keep that value at slow ptr index. Increment both counter. 
Keep count of number of zeros encountered to add them in the end


def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1=0
        n=len(nums)
        
        for ptr2 in range(n):
            if nums[ptr2]!=0:
                temp=nums[ptr2]
                nums[ptr2]=nums[ptr1]
                nums[ptr1]=temp
                ptr1+=1

        return nums

Optimal Soln: when we encounter val not 0, swap it with value present at slow. 
(Because mostly, this value will be filled with 0 in the end)
'''

'''
905. Sort array by parity
'''
# def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
#         n=len(nums)
        
#         left=0
#         right=n-1
        
#         while left<right:
           
#             if nums[left]%2==1 and nums[right]%2==0:
#                 temp=nums[left]
#                 nums[left]=nums[right]
#                 nums[right]=temp
                
#             if nums[right]%2==1:
#                 right-=1
            
#             if nums[left]%2==0:
#                 left+=1
            
#         return nums

'''
2 ptr approach: 1 at start, 1 at end.
if both are wrong swap. 

'''

'''
414. Third Maximum Number:
'''
# def thirdMax(self, nums: List[int]) -> int:
        
        
#         unique=[]
        
#         for i in nums:
#             if i not in unique:
#                 unique.append(i)
        
#         if len(unique)<3:
#             return max(unique)
        
#         else:
#             return sorted(unique,reverse=True)[2]

'''
Get all unique elements and sort the array, return third element from back.
'''

'''
448. Find all numbers disappeared in array
'''

# def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         for i in range(len(nums)):
#             val=abs(nums[i])-1
#             if nums[val]>0:
#                 nums[val]=-nums[val]
        
#         disapp=[]
#         for i in range(len(nums)):
#             if nums[i]>0:
#                 disapp.append(i+1)
#         return disapp
    
'''
1. for every element, go to index abs(element-1) and make it negative(check if it is not already negative).
2. In the end, check which elements are not negative. It means, their index+1 is not present.  
'''

'''
1413. Minimum Value to Get Positive Step by Step Sum
'''

# def minStartValue(self, nums: List[int]) -> int:

#         min_sum=0
#         prefix_sum=0
#         for i in range(len(nums)):
#             prefix_sum+=nums[i]
#             min_sum=min(prefix_sum,min_sum)
        
#         if min_sum==0:
#             return 1
#         else:
#             return abs(min_sum)+1

'''
Get prefix sum, and check the min sum (<0). If min is 0, return 1 
else return the abs(min_sum)

'''

'''
303. Range Sum Query
'''

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums=nums        

#     def sumRange(self, left: int, right: int) -> int:
#         sum=0
#         for i in range(left,right+1):
#             sum+=self.nums[i]
#         return sum

'''
Prefix Sum
'''

'''
1208. Get Equal strings within budget
'''

# def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

#         left=0
#         max_length=0
#         cost=0

#         for right in range(len(t)):
#             cost+=abs(ord(s[right])-ord(t[right]))
#             while(cost>maxCost):
#                 cost-=abs(ord(s[left])-ord(t[left]))
#                 left+=1
#             max_length=max(max_length,right-left+1)
        
#         return max_length


'''
Siding window: 
Condition: cost< maxcost
Update: length
'''

'''
1453. Max no. of vowels in a subtsring
'''
# def maxVowels(self, s: str, k: int) -> int:

#         vowels={'a':1,'e':1,'i':1,'o':1,'u':1}
        
#         count_vow=0
#         for i in range(k):
#             if s[i] in vowels:
#                 count_vow+=1
        
#         max_count=count_vow
#         for i in range(k,len(s)):
#             if s[i] in vowels:
#                 count_vow+=1
#             if s[i-k] in vowels:
#                 count_vow-=1
#             max_count=max(max_count,count_vow)

#         return max_count

'''
SLiding window: constant length:
check vowels in first window. Then add and remove the vowel count while sliding.
'''

'''
2000. Reverse Prefix of Word
'''

# def reversePrefix(self, word: str, ch: str) -> str:

#         word_l=list(word)
#         start=0
#         for i in range(len(word_l)):

#             if word_l[i]==ch:
#                 print(word_l)
#                 end=i
#                 while(start<end):
#                     temp=word_l[end]
#                     word_l[end]=word_l[start]
#                     word_l[start]=temp
#                     start+=1
#                     end-=1
#                 break
            
#         return ''.join(word_l)

'''
Go to that element, and reverse using 2 ptr: swap first and last, incr ptr.
'''

'''
557. Reverse words in a string 3
'''
# def reverseWords(self, s: str) -> str:

#         # s_list=s.split(' ')

#         # for words in range(len(s_list)):
#         #     s_list[words]=s_list[words][::-1]
        
#         # return ' '.join(s_list)

#         s_list=s.split(' ')

#         for i in range(len(s_list)):
#             left=0
#             right=len(s_list[i])-1
#             words=list(s_list[i])
#             while(left<right):
#                 temp=words[right]
#                 words[right]=words[left]
#                 words[left]=temp
#                 left+=1
#                 right-=1
#             s_list[i]=''.join(words)
            
#         return ' '.join(s_list)

'''
For every word, do reverse using 2 ptr.
'''

'''
Sliding window pattern:

for right in loop:
    right++
    while(condition):
        left++
    
    someupdate

No. of valid subarray= window size

'''

'''
713. Subarray Product Less than K
'''

# def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

#         if k<=1: return 0
#         prod=1
#         left=0
#         numsub=0

#         for right in range(len(nums)):
#             prod*=nums[right]
#             while(prod>=k):
#                 prod/=nums[left]
#                 left+=1
#             numsub+=right-left+1
        
#         return numsub

'''
487. Max Consecutive Ones 2:
'''
# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
#         left=0
#         count=0
#         max_ones=0

#         for right in range(len(nums)):

#             if nums[right]==0:
#                 count+=1
            
#             while(count>1):
#                 if nums[left]==0:
#                     count-=1
#                 left+=1
            
#             max_ones=max(max_ones,right-left+1)

#         return max_ones

'''
1004. Max Consecutive Ones 3
'''

# def longestOnes(self, nums: List[int], k: int) -> int:

#         left=0
#         count=0
#         max_ones=0

#         for right in range(len(nums)):

#             if nums[right]==0:
#                 count+=1
            
#             while(count>k):
#                 if nums[left]==0:
#                     count-=1
#                 left+=1

#             max_ones=max(max_ones,right-left+1)
        
#         return max_ones

'''
1493. Longest Subarray of 1's after deleting 1 element
'''
# def longestSubarray(self, nums: List[int]) -> int:

#         left=0
#         max_ones=0
#         count=0

#         for right in range(len(nums)):

#             if nums[right]==0:
#                 count+=1

#             while(count>1):
#                 if nums[left]==0:
#                     count-=1
#                 left+=1
            
#             max_ones=max(max_ones,right-left)

#         return max_ones

'''
340. Longest SUbstring with atmost k distinct characters
'''

# def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
#         left=0
#         hashmap={}
#         longest=0

#         for right in range(len(s)):
#             if s[right] not in hashmap:
#                 hashmap[s[right]]=1
#             elif s[right] in hashmap:
#                 hashmap[s[right]]+=1
           
#             while(len(hashmap)>k):
                
#                 hashmap[s[left]]-=1
#                 if hashmap[s[left]]==0:
#                     del hashmap[s[left]]
#                 left+=1
                
#             longest=max(longest,right-left+1)

#         return longest

'''
159. Longest SUbstring with atmost 2 distinct characters
'''

# def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
#         left=0
#         hashmap={}
#         longest=0

#         for right in range(len(s)):
#             if s[right] not in hashmap:
#                 hashmap[s[right]]=1
#             elif s[right] in hashmap:
#                 hashmap[s[right]]+=1
           
#             while(len(hashmap)>2):
                
#                 hashmap[s[left]]-=1
#                 if hashmap[s[left]]==0:
#                     del hashmap[s[left]]
#                 left+=1
                
#             longest=max(longest,right-left+1)

#         return longest

'''
268. Missing Number
'''

# def missingNumber(self, nums: List[int]) -> int:

#         n=len(nums)
#         expected_sum=(n*(n+1))//2
#         actual_sum=sum(nums)
#         return expected_sum-actual_sum