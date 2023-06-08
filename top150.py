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
6. 
'''