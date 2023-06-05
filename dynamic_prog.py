'''
Dynamic programming is technique for solving optimization problem, 
by breaking it down into simpler subproblems, and utilizing the fact that optimal solution 
to overall problems, depend on optimal solution to subproblems.

-we remember problems and answer ans reuse it

-optimization of divide and conquer

-Property of overlapping subproblems:

Approach:
- Top Down with Memoization: solve bigger prob by recursively finding solns to smaller subprobs.
storing the result of already solved subprobs: Memoization
'''

'''
Fibonacci using Memoization- O(n)
'''
# def fib(n,memo):
#     if n<=1:
#         return n
#     if n==2:
#         return 1
#     if n not in memo:
#         memo[n]=fib(n-1,memo)+fib(n-2,memo)
#     return memo[n]
# memo=dict()
# print(fib(5,memo))

'''
Approach 2: Tabulation- Bottom Up approach
-avoids recursion
-solves all related subprobs first, and filled in table
-soln to the top is then computed
'''
'''
Fibonacci with tabulation- O(n)
'''
# def fib(n): 
#     tab=[0,1]
#     for i in range(2,n+1):
#         tab.append(tab[i-1]+tab[i-2])
#     return tab[n-1]
    
# print(fib(6))

'''
Catalan Numbers
'''

# def catalan(n, memo):
#     if n<=1:
#         return 1
    
#     if n not in memo:
#         cat=0
#         for i in range(n):
#             if n in memo:
#                 memo[n]+=catalan(i, memo)*catalan(n-i-1, memo)
#             else:
#                 memo[n]=catalan(i, memo)*catalan(n-i-1, memo)
#     return memo[n] 
# memo={}
# print(catalan(5, memo))


        
'''
Number Factor- top down
'''
# def numFact(n,num_fact_dict):
#     if n<=2:
#         return 1
#     elif n==3:
#         return 2
#     elif n in num_fact_dict:
#         return num_fact_dict[n] 
#     else:
#         subP1=numFact(n-1,num_fact_dict)
#         subP2=numFact(n-3,num_fact_dict)
#         subP3=numFact(n-4,num_fact_dict)
#         num_fact_dict[n]=subP1+subP2+subP3
#         return num_fact_dict[n]

# print(numFact(5,{}))

# Bottom Up

# def numFact(n):
#     tab=[1,1,1,2]
#     for i in range(4,n+1):
#         tab.append(tab[i-1]+tab[i-3]+tab[i-4])
#     return tab[n]
# print(numFact(5))

'''
House Robber Problem- top down
'''
# def max_house(houses, currenthouse, amount):
#     if currenthouse>=len(houses):
#         return 0
#     elif currenthouse in amount:
#         return amount[currenthouse]
#     else:
#         opt1=houses[currenthouse]+max_house(houses,currenthouse+2, amount)
#         opt2=max_house(houses,currenthouse+1, amount)
#         amount[currenthouse]=max(opt1,opt2)
#         return amount[currenthouse]
    
# print(max_house([6,7,1,30,8,2,4],0,{}))

# Bottom Up

# def max_house(houses):
#     tab=[0]*(len(houses)+2)
#     for i in range(len(houses)-1,-1,-1):
#         tab[i]=max(houses[i]+tab[i+2],tab[i+1])
#     return tab[0]

# print(max_house([6,7,1,30,8,2,4]))

'''
Convert 1 string to another
'''
# def find_min_op(s1, s2, idx1, idx2, temp):
#     if idx1==len(s1):
#         return len(s2)-idx2
#     if idx2==len(s2):
#         return len(s1)-idx1
    
#     if s1[idx1]==s2[idx2]:
#         return find_min_op(s1,s2,idx1+1,idx2+1,temp)
    
#     else:
#         dictkey=str(idx1)+str(idx2)
#         if dictkey not in temp:
#             delop=1+find_min_op(s1,s2,idx1,idx2+1,temp)
#             insop=1+find_min_op(s1,s2,idx1+1,idx2,temp)
#             rep=1+find_min_op(s1,s2,idx1+1,idx2+1,temp)
#             temp[dictkey]=min(delop,insop,rep)
#         return temp[dictkey]
    
# print(find_min_op('table','tbrles',0,0,{}))

'''
Leet-152: Maximum product subarray
'''

# def maxProd(arr):
#     res=max(arr)
#     curMin, curMax=1,1
#     for n in arr:
#         if n==0:
#             curMax,curMin=1,1
#             continue
#         tmp=curMax*n
#         curMax=max(n*curMax,n*curMin,n)
#         curMin=min(tmp,n*curMin,n)
#         res=max(res,curMax)
#      return res

'''
Leet-300 Longest Increasing Subsequence:
'''

# def LongIS(nums):
#     LIS=[1]*len(nums)

#     for i in range(len(nums)-1,-1,-1):
#         for j in range(i+1, len(nums)):
#             if nums[i]<nums[j]:
#                 LIS[i]=max(LIS[i],1+LIS[j])
    
#     return max(LIS)

# O(n^2)

'''
Leet 1143- Longest Common subsequence:
'''
# def longcomsub(text1, text2):
#     dp=[[0 for j in range(len(text2+1))] for i in range(len(text1)+1)]

#     for i in range(len(text1)-1,-1,-1):
#         for j in range(len(text2)-1,-1,-1):
#             if text1[i]==text2[j]:
#                 dp[i][j]=1+dp[i+1][j+1]
#             else:
#                 dp[i][j]=max(dp[i+1][j],dp[i][j+1])

#     return dp[0][0]

'''
Leet 474- Zeroes and Ones 
'''

# def findmax(strs, m,n):
#     dp={}

#     def dfs(i,m,n):
#         if i==len(strs):
#             return 0
#         if (i,m,n) in dp:
#             return dp[(i,m,n)]

#         mCnt, nCnt=strs[i].count('0'),strs[i].count('1')
#         dp[(i,m,n)]=dfs(i+1,m,n)
#         if mCnt<=m and nCnt<=n:
#             dp[(i,m,n)]=max(dp[(i,m,n)],1+dfs(i+1,m-mCnt,n-nCnt))
#         return dp[(i,m,n)]

#     return dfs(0,m,n)

'''
Leet-72: Edit Distance
'''
# def minDist(word1,word2):
#     cache=[[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]

#     for j in range(len(word2)+1):
#         cache[len(word1)][j]=len(word2)-j
#     for i in range(len(word1)+1):
#         cache[j][len(word2)]=len(word2)-i

#     for i in range(len(word1)-1,-1,-1):
#         for j in range(len(word2)-1,-1,-1):
#             if word1[i]==word2[j]:
#                 cache[i][j]=cache[i+1][j+1]
#             else:
#                 cache[i][j]=1+min(cache[i+1][j],cache[i][j+1],cache[i+1][j+1])
    
#     return cache[0][0]

'''
Leet 64: Min Path Sum
'''
# def minPathSum(self, grid: List[List[int]]) -> int:
#     m=len(grid)
#     n=len(grid[0])
#     cache=[[float("inf")]*(n+1) for i in range(m+1)]
#     cache[m-1][n]=0

#     for i in range(m-1,-1,-1):
#         for j in range(n-1,-1,-1):
#             cache[i][j]=grid[i][j]+min(cache[i+1][j],cache[i][j+1]) 
#     return cache[0][0]

'''
Leet-322: Coin change
'''
# def coinChange(coins,amount):
#     dp=[amount+1]*(amount+1)
#     dp[0]=0
#     for a in range(1,amount+1):
#         for c in coins:
#             if a-c>=0:
#                 dp[a]=min(dp[a],1+dp[a-c])
#     return dp[amount] if dp[amount]!=amount+1 else -1

'''
Partition Equal Subset Sum:
'''

# if sum(nums)%2!=0:
#     return False
        
# target=sum(nums)/2
# n=len(nums)
# cache=set([0,nums[n-1]])
# for i in range(n-2,-1,-1):
#     temp=set()
#     for j in cache:
#         temp.add(nums[i]+j)
#         temp.add(j)

#     cache=temp

# if target in cache:
#     return True
# else:
#     return False

'''

'''



