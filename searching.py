'''
Linear Search- O(n)
'''

# def linearSearch(nums, target):
#     for i in range(nums):
#         if nums[i]==target:
#             return i
#     return -1

'''
Binary Search- O(LogN)
'''

# def bin_search(nums, target):
    
#     start=0
#     end=len(nums)-1
#     mid=(start+end)//2
#     while start<=end:
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]<target:
#             start=mid+1
#         else:
#             end=mid
#         mid=(start+end)//2
    
#     return -1

# print(bin_search([1,2,3,4,5],6))