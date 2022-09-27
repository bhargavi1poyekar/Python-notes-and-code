'''
Fibonacci Numbers- O(c^n)-> c -> number of calls
'''
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1)+fib(n-2)

# print(fib(6))

'''
Number Factor- No. of ways N can be expressed as sum of 1,3,4
'''

# def numFact(n):
#     if n<=2:
#         return 1
#     elif n==3:
#         return 2
#     else:
#         subP1=numFact(n-1)
#         subP2=numFact(n-3)
#         subP3=numFact(n-4)
#         return subP1+subP2+subP3

# print(numFact(5))

'''
House Robber

-Given n no. of housesalong the street with some amount of money
-Adjacent houses cannot be stolen
-Find max amount that can be stolen

Eg- 6,7,1,30,8,2,4

max=7+30+4=41

Divide into subprobs:

opt1: 6+f(5)  -> take first house, then we have options from the last 5 houses, 
as we have to skip the 2nd house

opt2: 0+f(6) -> skip first, and we have options from remaining 6 houses

'''
# def max_house(houses, currenthouse):
#     if currenthouse>=len(houses):
#         return 0
#     else:
#         opt1=houses[currenthouse]+max_house(houses,currenthouse+2)
#         opt2=max_house(houses,currenthouse+1)
#         return max(opt1,opt2)

# print(max_house([6,7,1,30,8,2,4],0))

'''
Convert 1 string to another:

-s1 and s2 are given
-convert s2 to s1 using delete, insert, or replace operations
-find min edit
'''
# def find_min_op(s1, s2, idx1, idx2):
#     if idx1==len(s1):
#         return len(s2)-idx2
#     if idx2==len(s2):
#         return len(s1)-idx1
    
#     if s1[idx1]==s2[idx2]:
#         return find_min_op(s1,s2,idx1+1,idx2+1)
    
#     else:
#         delop=1+find_min_op(s1,s2,idx1,idx2+1)
#         insop=1+find_min_op(s1,s2,idx1+1,idx2)
#         rep=1+find_min_op(s1,s2,idx1+1,idx2+1)
#         return min(delop,insop,rep)
    
# print(find_min_op('table','tbrles',0,0))

'''
Zero One Knapsack Problem
-Given profits and weights of N items
-Find max profit within given capacity of C
-Items cannot be broken
'''

# def knapsack(items, capacity, current_item):
#     if capacity<=0 or current_item<0 or current_item>=len(items):
#         return 0
#     elif items[current_item][1]<=capacity: #current_item[1]=>weight of item
#         prof1=items[current_item][0]+knapsack(items,capacity-items[current_item][1],current_item+1)
#         prof2=knapsack(items,capacity-items[current_item][1],current_item+1)
#         return max(prof1,prof2)
#     return 0

'''
Longest common subsequence:
- find len of longest subseq which is common to both strings
- subseq- seq obtained from string by deleting few items, without changing the order
'''

# def LCS(s1,s2,idx1,idx2):
#     if idx1>=len(s1) or idx2>=len(s2):
#         return 0
#     if s1[idx1]==s2[idx2]:
#         return 1+LCS(s1,s2,idx1+1,idx2+1)
#     else:
#         opt1=LCS(s1,s2,idx1+1,idx2)
#         opt2=LCS(s1,s2,idx1,idx2+1)
#         return max(opt1,opt2)

# print(LCS('elephant','erepat',0,0))

'''
Longest Palindromic subsequence
- Given a string S
- find len of lps in S
'''
# def LPS(s,st_idx,end_idx):
#     if st_idx>end_idx:
#         return 0
#     elif st_idx==end_idx:
#         return 1
#     if s[st_idx]==s[end_idx]:
#         return 2+LPS(s,st_idx+1,end_idx-1)
#     else:
#         opt1=LPS(s,st_idx+1,end_idx)
#         opt2=LPS(s,st_idx,end_idx-1)
#         return max(opt1,opt2)
    
# s='ELRMENMET'
# print(LPS(s,0,len(s)-1))

'''
Minimum cost to reach the last cell in 2d array:
- each cell has cost associated with it
- we can only go down or to the right cell
- find the min cost
'''

# def find_min_cost(array,i,j):
#     if i==-1 or j==-1:
#         return float('inf')
#     elif i==0 and j==0:
#         return array[i][j]
#     else:
#         opt1=find_min_cost(array,i-1,j)
#         opt2=find_min_cost(array,i,j-1)
#         # print(array[i][j])
#         return array[i][j]+min(opt1,opt2)

# both solution works, we can go from last to first, or first to last

# def find_min_cost(array,i,j):
#     if i==len(array) or j==len(array[0]):
#         return float('inf')
#     elif i==len(array)-1 and j==len(array)-1:
#         return array[i][j]
#     else:
#         opt1=find_min_cost(array,i+1,j)
#         opt2=find_min_cost(array,i,j+1)
#         # print(array[i][j])
#         return array[i][j]+min(opt1,opt2)


# array=[[4,7,8,6,4],
#        [6,7,3,9,2],
#        [3,8,1,2,4],
#        [7,1,7,3,7],
#        [2,9,8,9,3]]

# print(find_min_cost(array,0,0))

'''
Number of paths to reach the last cell with given cost
-cost is given, 
-everything else is similar to last prob
'''

# def num_paths(array, i, j, cost):
#     if cost<0:
#         return 0
#     elif i==0 and j==0:
#         if array[i][j]-cost==0:
#             return 1
#         else:
#             return 0
#     elif i==0:
#         return num_paths(array, 0, j-1, cost-array[i][j])
#     elif j==0:
#         return num_paths(array,i-1,0,cost-array[i][j])
#     else:
#         opt1=num_paths(array,i-1,j,cost-array[i][j])
#         opt2=num_paths(array,i,j-1,cost-array[i][j])
#         return opt1+opt2

# array=[[4,7,1,6],
#        [5,7,3,9],
#        [3,2,1,2],
#        [7,1,6,3]
#        ]
# print(len(array)-1,len(array[0])-1)

# print(num_paths(array,len(array)-1,len(array[0])-1,25))
    
'''
Longest nice substring- nice if the substring has both uppercase and lowercase of the letters present
'''

# def longestNiceSubstring(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
    
#         nice=''
#         for i in range(len(s)+1):
#             for j in range(len(s)+1):
#                 substr=s[i:j]
                
#                 if self.isNice(substr):
#                     print(substr)
#                     nice=max(nice,substr, key=len)
                
#         return nice
    
#     def isNice(self,s):
        
#         char_count=Counter(s)
        
#         for i in char_count:
#             if i.upper() not in s or i.lower() not in s:
#                 return False
#         return True

# Divide and Conquer approach:

# def longestNiceSubstring(s):
#         """
#         :type s: str
#         :rtype: str
#         """
    
#         idx=isNice(s)
#         if idx==-1:
#                 return s
        
#         opt1=longestNiceSubstring(s[0:idx])
#         opt2=longestNiceSubstring(s[idx+1:len(s)])
        
#         return max(opt1,opt2,key=len)
    
# def isNice(s):

#         char_pos={}
        
#         for i in range(len(s)):
#                 char_pos[s[i]]=i

#         for i in char_pos:
#                 if i.upper() not in s or i.lower() not in s:
#                         return char_pos[i]
#         return -1


# print(longestNiceSubstring('Bb'))

        