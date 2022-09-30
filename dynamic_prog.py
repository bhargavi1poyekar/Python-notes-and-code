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


