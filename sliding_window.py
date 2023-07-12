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
2260. Minimum Consecutive Cards to Pick up 
'''
#  def minimumCardPickup(self, cards: List[int]) -> int:

#         if len(cards)<2:
#             return -1

#         left=0
#         min_cards=float('inf')
#         hash_set=collections.Counter()
#         for right in range(0,len(cards)):
                
#                 while(hash_set[cards[right]]>=1):
#                     min_cards=min(min_cards,right-left+1)
#                     hash_set[cards[left]]-=1
#                     left+=1

#                 hash_set[cards[right]]+=1
            
                
#         return min_cards if min_cards!=float('inf') else -1

'''
2024. Maximize the Confusion of an Exam
'''

# def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
#         s=answerKey
#         maxAns=answerKey[0]
#         ansFreq=collections.Counter()
#         left=0

#         max_length=0

#         for right in range(len(answerKey)):
#             ansFreq[answerKey[right]]+=1

#             if ansFreq[answerKey[right]]>=ansFreq[maxAns]:
#                 maxAns=answerKey[right]
            
#             current_len=right-left+1

#             if(current_len-ansFreq[maxAns]>k):
#                 ansFreq[answerKey[left]]-=1
#                 left+=1
            
#             max_length=max(max_length,right-left+1)

#         return max_length