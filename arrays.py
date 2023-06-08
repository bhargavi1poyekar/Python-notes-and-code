
'''
Max Consecutive Ones
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
Find Numbers with even number of digits
'''
# def findNumbers(nums): 
#         digi_count=[0 for i in range(len(nums))]
#         print(digi_count)
#         for i in range(len(nums)):
                
#                 while(nums[i]!=0):
#                         nums[i]=nums[i]//10
#                         print(nums[i])
#                         digi_count[i]+=1
#                         print(digi_count)
                
        
#         even_count=0
#         for count in digi_count:
#                 if count%2==0:
#                         even_count+=1
#         return even_count

# print(findNumbers([555,901,482,1771]))

'''
Squares of sorted array => O(n)
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
Duplicate Zeros in place
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
Merge Sorted Arrays:
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
Check if N and its double exists
'''

# def checkIfExist(self, arr: List[int]) -> bool:
    
#     hash_tab={}
#     for i in arr:
#         if (2*i in hash_tab) or (i%2==0 and i//2 in hash_tab):
#             return True
#         hash_tab[i]=1
#     return False

'''
Valid Mountain Array
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
Replace Elements with greatest elements on right side
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
Move Zeros in the end
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
Sort array by parity
'''
# def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
#         n=len(nums)
        
#         left=0
#         right=n-1
        
#         while left<right and left<=n-1 and right>=0:
           
#             if nums[left]%2==1 and nums[right]%2==0:
#                 temp=nums[left]
#                 nums[left]=nums[right]
#                 nums[right]=temp
#                 left+=1
#                 right-=1
                
#             elif nums[left]%2==1 and nums[right]%2==1:
#                 right-=1
#             elif nums[left]%2==0 and nums[right]%2==1:
#                 left+=1
#                 right-=1
#             elif nums[left]%2==0 and nums[right]%2==0:
#                 left+=1
            
#         return nums

'''
Third Maximum Number:
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
Find all numbers disappeared in array
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
    
