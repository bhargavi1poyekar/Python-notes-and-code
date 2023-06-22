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

'''
Permutation in a string
'''

#  def checkInclusion(self, s1: str, s2: str) -> bool:
        
#         if len(s1)>len(s2):return False

#         s1_chars=[0 for i in range(26)]
#         s2_chars=[0 for i in range(26)]

#         for i in range(len(s1)):
#             s1_chars[ord(s1[i])-ord('a')]+=1
#             s2_chars[ord(s2[i])-ord('a')]+=1

#         match_count=0

#         for i in range(26):
#             if s1_chars[i]==s2_chars[i]:
#                 match_count+=1

#         start=0
#         for end in range(len(s1),len(s2)):
#             if match_count==26: return True
            
#             idx=ord(s2[end])-ord('a')
#             s2_chars[idx]+=1
#             if s1_chars[idx]==s2_chars[idx]:
#                 match_count+=1
#             elif s2_chars[idx]-1==s1_chars[idx]:
#                 match_count-=1
            
#             idx=ord(s2[start])-ord('a')
#             s2_chars[idx]-=1
#             if s1_chars[idx]==s2_chars[idx]:
#                 match_count+=1
#             elif s2_chars[idx]+1==s1_chars[idx]:
#                 match_count-=1
#             start+=1

#         return match_count==26 
