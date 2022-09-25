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
    
#     for i in range(1,len(nums)): # 0th element is in sorted arr
#         key=nums[i]   # first item of unsorted array
#         j=i-1         # last element of sorted arr
#         while j>=0 and key<nums[j]:  # till beginning of sorted arr and the key<element is sorted array
#             #check position in reverse
#             nums[j+1]=nums[j]    # move element one place forward
#             j-=1                 # go back one by one
#         nums[j+1]=key #finally place the element at its position
#     return nums

# print(insertionSort([8,7,6,5,4,3,2,1]))

'''
Merge Sort
'''

def merge(nums,l,m,r):
    
    n1=m-l+1 # size for first half
    n2=r-m   # size for second half
    
    # Create arrays for half with respective sizes
    arr1=[0]*(n1)
    arr2=[0]*(n2)
    
    # Distribute the nums values to the half arrays
    for i in range(0,n1):
        arr1[i]=nums[l+i]
    
    for j in range(0,n2):
        arr2[j]=nums[m+1+j]
        
        
    # Merge by sorting
    
    i=0
    j=0
    k=l
    
    # compare and add in ascending order till one of the half is empty
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            nums[k]=arr1[i]
            i+=1
        else:
            nums[k]=arr2[j]
            j+=1
        k+=1
    
    # if other half is empty, add the remaining of first half to merged
    while i<n1:
        nums[k]=arr1[i]
        i+=1
        k+=1
    
     # if other half is empty, add the remaining of second half to merged
    while j<n2:
        nums[k]=arr2[j]
        j+=1
        k+=1

    
def mergeSort(nums,l,r): # l=first index, r=last index
    if l<r: 
        m=(l+(r-1))//2 # find middle
        mergeSort(nums,l,m) # recursively send the halfves for mergesort
        mergeSort(nums,m+1,r) 
        merge(nums,l,m,r) # after breaking into individual items, merge them from bottom to top
    
    print(nums)

print(mergeSort([8,7,6,5,4,3,2,1],0,7))

'''
Quick sort
'''

def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums
 
 