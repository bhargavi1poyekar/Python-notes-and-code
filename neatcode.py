'''
Contains Duplicate
'''

# def containsDuplicate(self, nums: List[int]) -> bool:

#         # hash={}

#         # for num in nums:
#         #     if num in hash:
#         #         return True
#         #     else:
#         #         hash[num]=1
        
#         # return False

#         # nums=sorted(nums)

#         # for i in range(1,len(nums)):
#         #     if nums[i]==nums[i-1]:
#         #         return True
        
#         # return False


'''
isAnagram
'''

#  def isAnagram(self, s: str, t: str) -> bool:

#         if len(s)!=len(t):
#             return False

#         # s=sorted(s)
#         # t=sorted(t)

#         # if s==t:
#         #     return True
#         # return False


#         counter=[0 for i in range(26)]

#         for i in range(len(s)):
#             counter[ord(s[i])-ord('a')]+=1
#             counter[ord(t[i])-ord('a')]-=1
        
#         for count in counter:
#             if count!=0:
#                 return False
#         return True

'''
Two Sum
'''

# def twoSum(self, nums: List[int], target: int) -> List[int]:

#         hash={}

#         for i in range(len(nums)):
#             if nums[i] in hash:
#                 return [hash[nums[i]],i]
#             else:
#                 hash[target-nums[i]]=i

