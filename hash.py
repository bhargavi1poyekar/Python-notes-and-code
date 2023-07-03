'''
1426. Counting Elements
'''

# def countElements(self, arr: List[int]) -> int:

#         hash=set(arr)
#         count=0
#         for i in arr:
#             if i+1 in hash:
#                 count+=1
            
#         return count

'''
1941. Check if All Characters Have Equal Number of Occurrences
'''

# def areOccurrencesEqual(self, s: str) -> bool:

#         hash=collections.Counter()
#         for i in s:
#             hash[i]+=1
        
#         exp=len(s)//len(hash)
        
#         for i in hash:
#             if hash[i]!=exp:
#                 return False
#         return True

# -------------------------------------------------
#  return len(set(Counter(s).values())) == 1

'''
560. Subarray sum equals k
'''
#         hash=collections.Counter()
#         hash[0]=1
#         count=0
#         prefix_sum=0
#         for i in range(len(nums)):
#             prefix_sum+=nums[i]
#             count+=hash[prefix_sum-k]
#             hash[prefix_sum]+=1
#         return count

'''
1248. Count Number of Nice Subarrays:
'''
        # hash=collections.Counter()
        # hash[0]=1
        # odd_count=0
        # count=0
        
        # for i in nums:
        #     if i%2==1:
        #         odd_count+=1
        #     count+=hash[odd_count-k]
        #     hash[odd_count]+=1
        
        # return count

'''
2225. Find Players With Zero or One Losses
'''
# def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

       
        # loses=collections.Counter()
        
        # for i in range(len(matches)):
        #     loses[matches[i][0]]+=0
        #     loses[matches[i][1]]+=1
        
        
        # notlost=[]
        # lostone=[]
        # for i in loses:
        #     if loses[i]==0:
        #         notlost.append(i)
        #     elif loses[i]==1:
        #         lostone.append(i)
    
        # return [sorted(notlost),sorted(lostone)]

        # Since players are in the range of 0,len(matches):

        # loses=[-1 for i in range(100001)]

        # for i in matches:
        #     if loses[i[0]-1]==-1:
        #         loses[i[0]-1]=0
        #     if loses[i[1]-1]==-1:
        #         loses[i[1]-1]=1
        #     else:loses[i[1]-1]+=1

        # # print(loses)
        # notlost=[]
        # lostone=[]
       
        # for i in range(len(loses)):
        #     if loses[i]==0:
        #         notlost.append(i+1)
        #     elif loses[i]==1:
        #         lostone.append(i+1)
        # return [notlost,lostone]

'''
1133. Largest Unique Number.
'''

# def largestUniqueNumber(self, nums: List[int]) -> int:

#         hash=collections.Counter(nums)
#         unique=[]
#         for i in hash:
#             if hash[i]==1:
#                 unique.append(i)
        
#         return max(unique) if len(unique)!=0 else -1

'''
1189. Maximum Number of Balloons
'''
# def maxNumberOfBalloons(self, text: str) -> int:
        
#         balloon='balloon'
#         text_count=collections.Counter()
#         for i in text:
#             if i in balloon:
#                 text_count[i]+=1
        
#         for i in balloon:
#             if i not in text_count:
#                 text_count[i]=0
                
#         text_count['l']//=2
#         text_count['o']//=2

#         return min(text_count.values())

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
2352. Equal Row and Column Pairs
'''
# def equalPairs(self, grid: List[List[int]]) -> int:

#         rows=collections.Counter()
#         for row in grid:
#             rows[tuple(row)]+=1
        
#         cols=collections.Counter()
#         for col in range(len(grid[0])):
#             column=[]
#             for row in range(len(grid)):
#                 column.append(grid[row][col])
            
#             cols[tuple(column)]+=1
        
#         count=0
#         for elem in rows:
#             count+=rows[elem]*cols[elem]
        
#         return(count)


'''
771. Jewels and Stones
'''
# def numJewelsInStones(self, jewels: str, stones: str) -> int:

#         stones_count=collections.Counter(stones)
#         jewel_count=0
#         for j in jewels:
#             jewel_count+=stones_count[j]
        
#         return jewel_count

'''
1436. Destination City
'''
# def destCity(self, paths: List[List[str]]) -> str:

#         src=collections.Counter()
#         for i in paths:
#             src[i[0]]+=1
#             src[i[1]]+=0
        
#         for i in src:
#             if src[i]==0:
#                 return i

'''
1496. Path Crossing
'''

# def isPathCrossing(self, path: str) -> bool:

#         x=0
#         y=0
#         coord={}
#         coord[(0,0)]=1

#         for i in path:
#             if i=='N':
#                 y+=1
#             elif i=='S':
#                 y-=1
#             elif i=='E':
#                 x+=1
#             else:
#                 x-=1
#             # print(x,y,coord)
#             if (x,y) in coord:
#                 return True
#             else: coord[(x,y)]=1
        
#         return False

'''
1748. Sum of Unique Elements
'''
# def sumOfUnique(self, nums: List[int]) -> int:

#         unique=collections.Counter(nums)
        
#         sum=0
#         for i in unique:
#             if unique[i]==1:
#                 sum+=i
#         return sum


'''
451. Sort Characters By freq
'''

# def frequencySort(self, s: str) -> str:

#         freq=collections.Counter(s)
#         count=[[] for i in range(len(s)+1)]

#         for i in freq:
#             count[freq[i]].append(i)
            
#         ans=[]
#         for i in range(len(count)-1,0,-1):
#             for c in count[i]:
#                 ans.append(c*i)

#         return ''.join(ans)

'''
930. Binary Subarrays with Sum
'''

# def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

#         sums=collections.Counter()
#         sums[0]=1
#         count=0
#         pre_sum=0
#         for right in range(len(nums)):
#             pre_sum+=nums[right]
#             # print(pre_sum,count,sums)
#             if pre_sum-goal in sums:
#                 count+=sums[pre_sum-goal]
            
#             sums[pre_sum]+=1
#         return count

'''
1695. Max erasure value
'''

# def maximumUniqueSubarray(self, nums: List[int]) -> int:

#         left=0
#         hash_index={}
#         prefix_sum=[0]
#         for i in range(0,len(nums)):
#             prefix_sum.append(nums[i]+prefix_sum[i])
        

#         max_sum=0
       
        
#         for right in range(len(nums)):
            
#             if nums[right] in hash_index:
#                 max_sum=max(max_sum,prefix_sum[right]-prefix_sum[left])
#                 left=max(left,hash_index[nums[right]])
#             hash_index[nums[right]]=right+1
        
        
#         max_sum=max(max_sum,prefix_sum[right+1]-prefix_sum[left])
        
#         return(max_sum)


'''
1394. Find Lucky Integer in an Array
'''
# def findLucky(self, arr: List[int]) -> int:

#         lucky=[]
#         count=collections.Counter(arr)
#         # print(count)
#         for i in count:
#             if count[i]==i:
#                 lucky.append(i)

#         return max(lucky) if len(lucky)!=0 else -1


'''
1207. Unique Number of Occurrences
'''

# def uniqueOccurrences(self, arr: List[int]) -> bool:

#         arr_count=collections.Counter(arr)
#         count={}
#         for i in arr_count:
#             if arr_count[i] in count:
#                 return False
#             count[arr_count[i]]=i

#         return True

'''
1657. Determine If 2 strings are close.
'''

# def closeStrings(self, word1: str, word2: str) -> bool:

#         word1_count=collections.Counter(word1)
#         word2_count=collections.Counter(word2)

#         word1_keys=set(word1_count.keys())
#         word2_keys=set(word2_count.keys())

#         word1_values=sorted(word1_count.values())
#         word2_values=sorted(word2_count.values())

#         return True if word1_keys==word2_keys and word1_values==word2_values else False

'''
791. Custom String
'''

# def customSortString(self, order: str, s: str) -> str:

#         s_count=collections.Counter(s)

#         ans=[]
#         for char in order:
#             ans.append(char*s_count[char])
#             del s_count[char]
        
#         for i in s_count:
#             ans.append(i*s_count[i])

#         return ''.join(ans)