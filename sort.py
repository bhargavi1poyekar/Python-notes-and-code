'''
Bubble Sort
'''
# def bubbleSort(nums):
    
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
        
#     return nums
# print(bubbleSort([6,5,3,1,8,7,2,4]))

'''
Selection Sort
'''

# def selectionSort(nums):
    
#     min=0
    
#     for i in range(len(nums)):
#         min=i # New min for every iteration
#         for j in range(i,len(nums)):
#             if nums[j]<nums[min]: # Find smallest element in the array
#                 min=j
#         nums[i],nums[min]=nums[min],nums[i] #Swap it with start index
        
            
#     return nums
    
# print(selectionSort([8,7,6,5,4,3,2,1]))


'''
Insertion Sort
'''
# def insertionSort(nums):
    
#     for i in range(len(nums)):
#         if nums[i]<nums[0]:
#             nums.insert(0,nums[i])
#         else:
#             for j in range(1,len(nums)):
#                 if(nums[i]>nums[j-1] and nums[i]<nums[j]):
#                     nums.insert(j,nums[i])
#     return nums

# print(insertionSort([8,7,6,5,4,3,2,1]))